from .stream import Stream
from .cam_video_stream import CamVideoStream
from .file_video_stream import FileVideoStream
from typing import Union
from pathlib import Path


class StreamCreator:
    @staticmethod
    def create_stream(src: Union[int, str] = 0,
                      is_realtime: bool = None,
                      buffer_size: int = 128) -> Stream:
        stream = None

        if isinstance(src, int):
            is_realtime = True if is_realtime is None else is_realtime
            stream = CamVideoStream(src, is_realtime, buffer_size)

        if isinstance(src, str):
            if Path(src).exists():
                stream = FileVideoStream(src, buffer_size)

        return stream
