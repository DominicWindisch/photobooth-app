#!/usr/bin/python3
"""
Photobooth Application start script
"""
import subprocess
import os
import sys
import platform
import logging
import asyncio
import uuid
import multiprocessing
import socket
from asyncio import Queue, QueueFull
from pathlib import Path
import uvicorn
import psutil
from sse_starlette import EventSourceResponse, ServerSentEvent
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import HTTPException as StarletteHTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from fastapi.responses import (
    StreamingResponse,
    FileResponse,
    Response,
)
from fastapi import FastAPI, Request, HTTPException, status
from pymitter import EventEmitter
from src.imageservers import ImageServers
from src.informationservice import InformationService
from src.configsettings import ConfigSettings, settings
from src.keyboardservice import KeyboardService
from src.processingpicture import ProcessingPicture
from src.wledservice import WledService
from src.imagedb import ImageDb
from src.loggingservice import LoggingService

# from gpiozero import CPUTemperature, LoadAverage


# constants
SERVICE_NAME = "imageserver"

# create early instances
# event system and logging
ee: EventEmitter = EventEmitter()
ls: LoggingService = LoggingService(evtbus=ee)


logger = logging.getLogger(__name__)
app = FastAPI(docs_url="/api/doc", redoc_url=None, openapi_url="/api/openapi.json")


@app.get("/eventstream")
async def subscribe(request: Request):
    """
    Eventstream to feed clients with server generated events and data
    """

    # local message queue, each client has it's own queue
    # limit max queue size in case client doesnt catch up so fast.
    # if there are more than 100 messages in the queue
    # it can be assumed that the connection is broken or something.
    # Queue changed in python 3.10, for compatiblity subscribe is
    # async since queue reuses the async thread
    # that would not be avail if outer function of queue is sync.
    # https://docs.python.org/3.11/library/asyncio-queue.html
    queue = Queue(100)

    def add_subscriptions():
        logger.debug(f"SSE subscription added, client {request.client}")
        ee.on("publishSSE", add_queue)

    def remove_subscriptions():
        ee.off("publishSSE", add_queue)
        logger.debug(f"SSE subscription removed, client {request.client}")

    def add_queue(sse_event, sse_data):
        try:
            queue.put_nowait(
                ServerSentEvent(
                    id=uuid.uuid4(), event=sse_event, data=sse_data, retry=10000
                )
            )
        except QueueFull as exc:
            # actually never run, because queue size is infinite currently
            remove_subscriptions()
            logger.error(
                f"SSE queue full! event '{sse_event}' not sent. Connection broken?"
            )
            raise HTTPException(
                status_code=500,
                detail=f"SSE queue full! event '{sse_event}' not sent. Connection broken?",
            ) from exc

    async def event_iterator():
        try:
            while True:
                if await request.is_disconnected():
                    remove_subscriptions()
                    logger.info(f"client request disconnect, client {request.client}")
                    break

                event = await queue.get()

                # send data to client
                yield event

        except asyncio.CancelledError:
            remove_subscriptions()
            logger.info(f"Disconnected from client {request.client}")

    logger.info(f"Client connected {request.client}")
    add_subscriptions()

    # initial messages on client connect
    add_queue(sse_event="message", sse_data=f"Client connected {request.client}")

    # all modules can register this event to send initial messages on connection
    await ee.emit_async("publishSSE/initial")

    return EventSourceResponse(event_iterator(), ping=1)


@app.get("/config/ui")
def api_get_config_ui():
    """get part of the config dedicated for UI only. UI requests this on startup"""
    return ConfigSettings().uisettings.dict()


@app.get("/config/schema")
def api_get_config_schema(schema_type: str = "default"):
    """
    Get schema to build the client UI
    :param str schema_type: default or dereferenced.
    """
    return settings.get_schema(schema_type=schema_type)


@app.get("/config/currentActive")
def api_get_config_current_active():
    """returns currently cached and active settings"""
    return settings.dict()


@app.get("/config/current")
def api_get_config_current():
    """read settings from drive and return"""
    return ConfigSettings().dict()


@app.post("/config/current")
def api_post_config_current(updated_settings: ConfigSettings):
    updated_settings.persist()  # save settings to disc
    # restart service to load new config
    util_systemd_control("restart")


@app.get("/api/imageservers/capturemode", status_code=status.HTTP_202_ACCEPTED)
def api_cmd_imageserver_capturemode_get(wled_control: bool = True):
    """_summary_

    Args:
        wled_control (bool, optional): Also control wled module. Request WLED module preset thrill. Defaults to True.
    """
    ee.emit("onCaptureMode")
    if wled_control:
        ee.emit("wled/preset_thrill")


@app.get("/api/imageservers/previewmode", status_code=status.HTTP_202_ACCEPTED)
def api_cmd_imageserver_previewmode_get(wled_control: bool = True):
    """_summary_

    Args:
        wled_control (bool, optional): Also control wled module. Request WLED module preset standby. Defaults to True.
    """
    ee.emit("onPreviewMode")
    if wled_control:
        ee.emit("wled/preset_standby")


@app.get("/cmd/{action}/{param}")
def api_cmd(action, param):
    logger.info(f"cmd api requested action={action}, param={param}")

    if action == "config" and param == "reset":
        settings.deleteconfig()
        util_systemd_control("restart")
    elif action == "config" and param == "restore":
        os.system("reboot")
    elif action == "server" and param == "reboot":
        os.system("reboot")
    elif action == "server" and param == "shutdown":
        os.system("shutdown now")
    elif action == "service" and param == "restart":
        util_systemd_control("restart")
    elif action == "service" and param == "stop":
        util_systemd_control("stop")
    elif action == "service" and param == "start":
        util_systemd_control("start")

    else:
        raise HTTPException(500, f"invalid request action={action}, param={param}")

    return f"action={action}, param={param}"


def util_systemd_control(state):
    # will return 0 for active else inactive.
    try:
        subprocess.run(
            args=["systemctl", "--user", "is-active", "--quiet", SERVICE_NAME],
            timeout=10,
            check=True,
        )
    except FileNotFoundError:
        logger.info(
            f"command systemctl not found to invoke restart; restart {SERVICE_NAME} by yourself."
        )
    except subprocess.CalledProcessError as exc:
        # non zero returncode
        logger.warning(
            f"service {SERVICE_NAME} currently inactive, need to restart by yourself! error {exc}"
        )
    except subprocess.TimeoutExpired as exc:
        logger.error(f"subprocess timeout {exc}")
    else:
        # no error, service restart ok
        logger.info(f"service {SERVICE_NAME} currently active, restarting")
        os.system(f"systemctl --user {state} {SERVICE_NAME}")


@app.get("/cmd/capture")
@app.get("/chose/1pic")
def api_chose_1pic_get():
    if not processingpicture.idle.is_active:
        raise HTTPException(
            status_code=400,
            detail="bad request, only one request at a time!",
        )

    try:
        processingpicture.thrill()
        processingpicture.countdown()
        processingpicture.shoot()
        processingpicture.postprocess()
        processingpicture.finalize()

        return "OK"
    except Exception as exc:
        logger.exception(exc)
        raise HTTPException(
            status_code=500,
            detail=f"something went wrong, Exception: {exc}",
        ) from exc


@app.get(
    "/api/imageservers/still",
    # Set what the media type will be in the autogenerated OpenAPI specification.
    # fastapi.tiangolo.com/advanced/additional-responses/#additional-media-types-for-the-main-response
    responses={200: {"content": {"image/jpeg": {}}}},
    # Prevent FastAPI from adding "application/json" as an additional
    # response media type in the autogenerated OpenAPI specification.
    # https://github.com/tiangolo/fastapi/issues/3258
    response_class=Response,
)
def api_still_get():
    """Aquire image and serve to download

    Raises:
        HTTPException: Image could not be aquired from backend

    Returns:
        Response: Returns jpeg image to download
    """
    try:
        still_image: bytes = bytes(imageServers.wait_for_hq_image())
        logger.info(f"aquired still_image {len(still_image)}bytes to be send to client")
        return Response(still_image, media_type="image/jpeg")
    except Exception as exc:
        logger.exception(exc)
        raise HTTPException(
            status_code=500,
            detail=f"something went wrong, Exception: {exc}",
        ) from exc


@ee.on("keyboardservice/chose_1pic")
def evt_chose_1pic_get():
    if not processingpicture.idle.is_active:
        raise RuntimeError("bad request, only one request at a time!")

    processingpicture.thrill()
    processingpicture.countdown()
    processingpicture.shoot()
    processingpicture.postprocess()
    processingpicture.finalize()


@app.get("/gallery/images")
def api_gallery_images():
    try:
        return imageDb.db_get_images()
    except Exception as exc:
        logger.exception(exc)
        raise HTTPException(
            status_code=500, detail=f"something went wrong, Exception: {exc}"
        ) from exc


@app.get("/gallery/delete", status_code=status.HTTP_204_NO_CONTENT)
def api_gallery_delete(image_id: str):
    logger.info(f"gallery_delete requested, id={image_id}")
    try:
        imageDb.delete_image_by_id(image_id)
    except Exception as exc:
        logger.exception(exc)
        raise HTTPException(500, f"deleting failed: {exc}") from exc


@app.get("/gallery/delete_all", status_code=status.HTTP_204_NO_CONTENT)
def api_gallery_delete_all():
    """Warning: deletes all files permanently without any further confirmation

    Raises:
        HTTPException: _description_
    """
    logger.info("delete_all media items requested")
    try:
        imageDb.delete_images()
        logger.info("all media successfully deleted")
    except Exception as exc:
        logger.exception(exc)
        raise HTTPException(500, f"deleting all media items failed: {exc}") from exc


@app.get("/stream.mjpg")
def video_stream():
    """
    endpoint to stream live video to clients
    """
    if not settings.backends.LIVEPREVIEW_ENABLED:
        raise HTTPException(405, "preview not enabled")

    headers = {"Age": "0", "Cache-Control": "no-cache, private", "Pragma": "no-cache"}

    try:
        return StreamingResponse(
            imageServers.gen_stream(),
            headers=headers,
            media_type="multipart/x-mixed-replace; boundary=frame",
        )
    except Exception as exc:
        logger.exception(exc)
        raise HTTPException(500, f"preview failed: {exc}") from exc


# serve data directory holding images, thumbnails, ...
app.mount("/data", StaticFiles(directory="data"), name="data")


@app.get("/log/latest")
def get_qbooth_log():
    """provide latest logfile to download
    TODO Handle exception if file not exists

    Returns:
        _type_: _description_
    """
    # might be a bug in fastapi: if file changes after file length determined
    # for header content-length, the browser rejects loading the file.
    # return FileResponse(path="./log/qbooth.log")

    return Response(
        content=Path("./log/qbooth.log").read_text(encoding="utf-8"),
        media_type="text/plain",
    )


@app.get("/")
def read_index():
    """
    return homepage of booth
    """
    headers = {"Cache-Control": "no-store, no-cache, must-revalidate"}
    return FileResponse(path="web/index.html", headers=headers)


# if not match anything above, default to deliver static files from web directory
app.mount("/", StaticFiles(directory="web"), name="web")


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    logger.error(f"http StarletteHTTPException: {repr(exc)}")
    return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    logger.error(f"http RequestValidationError: {exc}")
    return await request_validation_exception_handler(request, exc)


if __name__ == "__main__" or "PYTEST_CURRENT_TEST" in os.environ:
    # all dependencies that access hardware are loaded here in if condition
    # reason: due to using backends with separate processes, this file is executed again per process
    # so hardware would be accessed two times when using backends with sep processes - no bueno
    # We are running under pytest or started the program. setup the dependencies.
    logger.info("setting up dependencies")

    # guard to start only one instance at a time.
    try:
        s = socket.socket()
        s.bind(("localhost", 19988))  # bind fails on second instance, raising OSError
    except OSError:
        logger.error("startup aborted. another instance is running. exiting.")
        sys.exit(-1)

    # set spawn for all systems (defaults fork on linux currently and spawn on windows platform)
    # spawn will be the default for all systems in future so it's set here now to have same
    # results on all platforms
    multiprocessing_start_method = multiprocessing.get_start_method(allow_none=True)
    logger.info(f"{multiprocessing_start_method=}, before forcing")
    multiprocessing.set_start_method(method="spawn", force=True)
    multiprocessing_start_method = multiprocessing.get_start_method(allow_none=True)
    logger.info(f"{multiprocessing_start_method=}, forced")

    wledservice = WledService(ee)
    # load imageserver dynamically because service can be configured
    # https://stackoverflow.com/a/14053838
    imageServers = ImageServers(ee)
    imageDb = ImageDb(ee, imageServers.primary_backend)
    ks = KeyboardService(ee)
    ins = InformationService(ee, imageServers)
    processingpicture = ProcessingPicture(ee, imageServers, imageDb)

if __name__ == "__main__":
    # here is the server started

    logger.info("Welcome to qPhotobooth")
    logger.info(f"{platform.system()=}")
    logger.info(f"{platform.release()=}")
    logger.info(f"{platform.machine()=}")
    logger.info(f"{platform.python_version()=}")
    logger.info(f"{platform.node()=}")
    logger.info(f"{psutil.cpu_count()=}")
    logger.info(f"{psutil.cpu_count(logical=False)=}")
    logger.info(f"{psutil.disk_partitions()=}")
    if platform.system() == "Linux":
        logger.info(f"{psutil.disk_usage('/')=}")
    elif platform.system() == "Windows":
        logger.info(f"{psutil.disk_usage('C:')=}")
    logger.info(
        [
            (name, [addr.address for addr in addrs if addr.family == socket.AF_INET])
            for name, addrs in psutil.net_if_addrs().items()
        ]
    )
    logger.info(f"{psutil.virtual_memory()=}")
    # run python with -O (optimized) sets debug to false and disables asserts from bytecode
    logger.info(f"{__debug__=}")

    # start services
    imageServers.start()
    ins.start()
    try:
        wledservice.start()
    except RuntimeError as wledservice_exc:
        # catch exception to make app continue without wled service in case there is a connection problem
        logger.warning(f"WLED module init failed {wledservice_exc}")

    # log_level="trace", default info
    config = uvicorn.Config(
        app=app,
        host="0.0.0.0",
        port=settings.common.webserver_port,
        log_level="info",
    )
    server = uvicorn.Server(config)

    """
    shutdown app workaround:
    workaround until https://github.com/encode/uvicorn/issues/1579 is fixed and
    shutdown can be handled properly.
    Otherwise the stream.mjpg if open will block shutdown of the server
    signal CTRL-C and systemctl stop would have no effect, app stalls

    signal.signal(signal.SIGINT, signal_handler) and similar
    don't work, because uvicorn is eating up signal handler
    currently: https://github.com/encode/uvicorn/issues/1579
    the workaround: currently we set force_exit to True to shutdown the server
    """
    server.force_exit = True

    ls.uvicorn()

    # serve files forever, loops endless
    server.run()

    # shutdown services
    wledservice.stop()
    imageServers.stop()
    ins.stop()
