from .stream import Stream
from .cam_video_stream import CamVideoStream
from .file_video_stream import FileVideoStream
from .network_video_stream import NetworkVideoStream
from typing import Union
from pathlib import Path


class StreamCreator:
    @staticmethod
    def create_stream(src: Union[int, str] = 0,
                      is_live: bool = None,
                      buffer_size: int = 128) -> Stream:
        stream = None

        if isinstance(src, int):
            is_live = True if is_live is None else is_live
            stream = CamVideoStream(src, is_live, buffer_size)

        if isinstance(src, str):
            if Path(src).exists():
                stream = FileVideoStream(src, buffer_size)
            else:
                stream = NetworkVideoStream(src, is_live=is_live, buffer_size=128)

        return stream
