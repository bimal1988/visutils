from .video_input_stream import VideoInputStream
from .cam_video_input_stream import CamVideoInputVideoInputStream
from .file_video_input_stream import FileVideoInputVideoInputStream
from .network_video_input_stream import NetworkVideoInputVideoInputStream
from .youtube_video_input_stream import YoutubeVideoInputVideoInputStream
from typing import Union
from pathlib import Path


class StreamCreator:
    @staticmethod
    def create_video_input_stream(src: Union[int, str] = 0,
                                  is_live: bool = None,
                                  buffer_size: int = 128) -> VideoInputStream:
        stream = None

        if isinstance(src, int):
            is_live = True if is_live is None else is_live
            stream = CamVideoInputVideoInputStream(src, is_live, buffer_size)

        if isinstance(src, str):
            if src.startswith('http'):
                stream = YoutubeVideoInputVideoInputStream(src, False, buffer_size)
            elif Path(src).exists():
                stream = FileVideoInputVideoInputStream(src, buffer_size)
            else:
                stream = NetworkVideoInputVideoInputStream(src, is_live=is_live, buffer_size=128)

        return stream
