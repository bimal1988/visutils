from .stream import Stream
from .types import AsyncMode
from .async_video_capture import create_async_video_capture


class WebcamVideoStream(Stream):
    def __init__(self,
                 src: int,
                 use_buffer: bool,
                 buffer_size: int,
                 async_mode: AsyncMode):
        self._realtime = not use_buffer
        self._cap = create_async_video_capture(src, async_mode)

    def start(self):
        self._cap.start()

    def stop(self):
        self._cap.stop()

    def read(self):
        return self._cap.read()
