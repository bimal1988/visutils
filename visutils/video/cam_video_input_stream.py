from typing import Union

from .threaded_video_capture import ThreadedVideoCapture
from .video_input_stream import VideoInputStream


class CamVideoInputStream(VideoInputStream):
    """Creates a video input stream to read from camera"""
    def __init__(self, src: Union[int, str], **kwargs):
        """
        Args:
            src (int): Camera index or device path
            **kwargs: OpenCV VideoCapture Properties. See references.
        References:
        `OpenCV VideoCapture Properties <https://docs.opencv.org/3.4/d4/d15/
        group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d>`_
        """
        self._cap = ThreadedVideoCapture(src, is_live=True, buffer_size=1,
                                         **kwargs)

    def start(self):
        self._cap.start()

    def stop(self):
        self._cap.stop()

    def read(self):
        return self._cap.read()
