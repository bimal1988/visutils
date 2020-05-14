from .video_input_stream import VideoInputStream
from .cam_video_input_stream import CamVideoInputVideoInputStream
from .file_video_input_stream import FileVideoInputVideoInputStream
from .network_video_input_stream import NetworkVideoInputVideoInputStream
from .youtube_video_input_stream import YoutubeVideoInputVideoInputStream
from .screen_grab_video_input_stream import ScreenGrabVideoInputStream
from visutils.common.path_utils import SourceType, get_source_type
from typing import Union


class StreamCreator:
    @staticmethod
    def create_video_input_stream(src: Union[int, str] = 0,
                                  is_live: bool = None,
                                  buffer_size: int = 128) -> VideoInputStream:
        stream = None
        source_type = get_source_type(src)

        if source_type is SourceType.CAMERA:
            is_live = True if is_live is None else is_live
            stream = CamVideoInputVideoInputStream(src, is_live, buffer_size)
        elif source_type is SourceType.FILE:
            stream = FileVideoInputVideoInputStream(src, buffer_size)
        elif source_type is SourceType.NETWORK:
            stream = NetworkVideoInputVideoInputStream(src, is_live=is_live, buffer_size=128)
        elif source_type is SourceType.YOUTUBE:
            stream = YoutubeVideoInputVideoInputStream(src, False, buffer_size)
        elif source_type is SourceType.PICAMERA:
            from .picam_video_input_stream import PicamVideoInputStream
            stream = PicamVideoInputStream(src)
        else:
            stream = ScreenGrabVideoInputStream()

        return stream
