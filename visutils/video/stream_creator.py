from typing import Union

from visutils.common.path_utils import get_source_type, SourceType
from .cam_video_input_stream import CamVideoInputStream
from .file_video_input_stream import FileVideoInputStream
from .network_video_input_stream import NetworkVideoInputStream
from .screen_grab_video_input_stream import ScreenGrabVideoInputStream
from .video_input_stream import VideoInputStream
from .youtube_video_input_stream import YoutubeVideoInputVideoInputStream


def create_video_input_stream(src: Union[int, str] = 0,
                              is_live: bool = None,
                              buffer_size: int = 128) -> VideoInputStream:
    stream = None
    source_type = get_source_type(src)

    if source_type is SourceType.CAMERA:
        stream = CamVideoInputStream(src)
    elif source_type is SourceType.FILE:
        stream = FileVideoInputStream(src, buffer_size)
    elif source_type is SourceType.NETWORK:
        stream = NetworkVideoInputStream(src, is_live=is_live,
                                         buffer_size=128)
    elif source_type is SourceType.YOUTUBE:
        stream = YoutubeVideoInputVideoInputStream(src, False, buffer_size)
    elif source_type is SourceType.PICAMERA:
        from .picam_video_input_stream import PicamVideoInputStream
        stream = PicamVideoInputStream(src)
    else:
        stream = ScreenGrabVideoInputStream()

    return stream
