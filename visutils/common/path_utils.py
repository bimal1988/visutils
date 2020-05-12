from pathlib import Path
from urllib.parse import urlparse
from typing import Union
from enum import Enum


class SourceType(Enum):
    CAMERA = 0
    FILE = 1
    YOUTUBE = 2
    NETWORK = 3
    PICAMERA = 4


def get_source_type(path: Union[int, str]) -> SourceType:
    if isinstance(path, int) or path.startswith('/dev/'):
        return SourceType.CAMERA
    elif isinstance(path, str):
        parsed_url = urlparse(path)
        scheme = parsed_url.scheme
        netloc = parsed_url.netloc

        if not scheme and Path(path).exists():
            return SourceType.FILE
        elif scheme in ['http', 'https'] \
                and netloc.lstrip('www.') in ['youtube.com', 'youtu.be']:
            return SourceType.YOUTUBE
        elif scheme in ['http', 'https', 'rtp', 'rtsp', 'rtmp', 'tcp', 'udp']:
            return SourceType.NETWORK
        elif path.lower() == 'picamera':
            return SourceType.PICAMERA
