from .types import AsyncMode
from .stream import Stream
from .webcam_video_stream import WebcamVideoStream
from typing import Union


class StreamCreator:
    @staticmethod
    def create_stream(src: Union[int, str] = 0,
                      use_buffer: bool = False,
                      buffer_size: int = 128,
                      async_mode=AsyncMode.MULTI_THREADING) -> Stream:
        stream = None

        if isinstance(src, int):
            stream = WebcamVideoStream(src, use_buffer, buffer_size, async_mode)

        return stream
