from pymitter import EventEmitter
from src.configsettings import settings
import pytest
import platform
import logging
from .utils import get_images

logger = logging.getLogger(name=None)

"""
prepare config for testing
"""


## check skip if wrong platform
if not platform.system() == "Linux":
    pytest.skip(
        "v4l is linux only platform, skipping test",
        allow_module_level=True,
    )

## tests


def test_getImages():
    from src.imageserverwebcamv4l import ImageServerWebcamV4l, available_camera_indexes

    _availableCameraIndexes = available_camera_indexes()
    if not _availableCameraIndexes:
        pytest.skip("no camera found, skipping test")

    cameraIndex = _availableCameraIndexes[0]

    logger.info(f"available camera indexes: {_availableCameraIndexes}")
    logger.info(f"using first camera index to test: {cameraIndex}")

    # modify config:
    settings.backends.v4l_device_index = cameraIndex

    # ImageServerSimulated backend: test on every platform
    backend = ImageServerWebcamV4l(EventEmitter(), True)

    get_images(backend)
