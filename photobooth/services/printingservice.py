"""
Handle all media collection related functions
"""
import subprocess
import time
from datetime import datetime
from pathlib import Path

from PIL import Image

from .baseservice import BaseService
from .config import appconfig
from .mediacollection.mediaitem import PATH_PRINT, MediaItem
from .mediacollectionservice import MediacollectionService
from .mediaprocessing.print_pipelinestages import merge_print_items_stage
from .sseservice import SseEventFrontendNotification, SseService

TIMEOUT_PROCESS_RUN = 6  # command to print needs to complete within 6 seconds.


class PrintingService(BaseService):
    """Handle all image related stuff"""

    def __init__(self, sse_service: SseService, mediacollection_service: MediacollectionService):
        super().__init__(sse_service)

        # common objects
        self._mediacollection_service: MediacollectionService = mediacollection_service

        # custom service objects
        self._last_print_time = None
        self._printing_queue = None  # TODO: could add queue later

    def start(self):
        # unblock after restart immediately
        self._last_print_time = None

    def stop(self):
        pass

    def print(self, mediaitems: list[MediaItem]):
        ## print mediaitem

        if not appconfig.hardwareinputoutput.printing_enabled:
            raise ConnectionRefusedError("Printing is disabled! Enable in config first.")

        # block queue new prints until configured time is over
        if self.is_blocked():
            raise BlockingIOError(f"Print request ignored! Wait {self.remaining_time_blocked():.0f}s before try again.")

        # convert images into print layout pages
        images_to_print: list[Image.Image] = [Image.open(item.path_full.absolute()) for item in mediaitems]
        pages_to_print = merge_print_items_stage(
            images_to_print, appconfig.hardwareinputoutput.print_medium_width_mm, appconfig.hardwareinputoutput.print_medium_height_mm, 0.1, 300
        )

        base_name = f"print_layout_{datetime.now().astimezone().strftime('%Y%m%d-%H%M%S-%f')}"
        for page_index, page in enumerate(pages_to_print):
            # filename absolute to print, use in printing command

            filename = Path(PATH_PRINT, f"{base_name}_{page_index}.jpeg").absolute()
            page.save(filename)

            try:
                # print command
                self._logger.info(f"printing {filename=}")

                completed_process = subprocess.run(
                    str(appconfig.hardwareinputoutput.printing_command).format(filename=filename),
                    capture_output=True,
                    check=True,
                    timeout=TIMEOUT_PROCESS_RUN,
                    shell=True,  # needs to be shell so a string as command is accepted.
                )

                self._logger.info(f"cmd={completed_process.args}")
                self._logger.info(f"stdout={completed_process.stdout}")
                self._logger.debug(f"stderr={completed_process.stderr}")

                self._logger.info(f"print command started successfully {filename}")

                # update last print time to calc block time on next run
                self._start_time_blocked()
            except Exception as exc:
                self._sse_service.dispatch_event(SseEventFrontendNotification(color="negative", message=f"{exc}", caption="Print Error"))
                raise RuntimeError(f"print failed, error {exc}") from exc

    def is_blocked(self):
        return self.remaining_time_blocked() > 0.0

    def remaining_time_blocked(self) -> float:
        if self._last_print_time is None:
            return 0.0

        delta = time.time() - self._last_print_time
        if delta >= appconfig.hardwareinputoutput.printing_blocked_time:
            # last print is longer than configured time in the past - return 0 to indicate no wait time
            return 0.0
        else:
            # there is some time to wait left.
            return appconfig.hardwareinputoutput.printing_blocked_time - delta

    def _start_time_blocked(self):
        self._last_print_time = time.time()

        # TODO: add some timer/coroutine to send regular update to UI with current remaining time blocked

    def _print_timer_fun(self):
        ## thread to send updates to client about remaining blocked time
        pass
