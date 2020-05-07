from .types import AsyncMode
from .mt_video_capture import MTVideoCapture
from .mp_video_capture import MPVideoCapture


def create_async_video_capture(source, async_mode):
    if async_mode is AsyncMode.MULTI_THREADING:
        return MTVideoCapture(source)
    elif async_mode is AsyncMode.MULTI_PROCESSING:
        return MPVideoCapture(source)
