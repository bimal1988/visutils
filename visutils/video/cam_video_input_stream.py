from typing import Union

from .threaded_video_capture import ThreadedVideoCapture
from .video_input_stream import VideoInputStream


class CamVideoInputStream(VideoInputStream):
    """Creates a video input stream to read from camera"""

    def __init__(self, src: Union[int, str], **kwargs):
        """
        Args:
            src: Camera index or device path.
        Keyword Args:
            CAP_PROP_FRAME_WIDTH: Width of the frames in the video stream.
            CAP_PROP_FRAME_HEIGHT: Height of the frames in the video stream.
            CAP_PROP_POS_MSEC: Current position of the video file in
                milliseconds.
            CAP_PROP_POS_FRAMES: 0-based index of the frame to be
                decoded/captured next.
            CAP_PROP_POS_AVI_RATIO: Relative position of the video file:
                0=start of the film, 1=end of the film.
            CAP_PROP_FPS: Frame rate.
            CAP_PROP_FRAME_COUNT: Number of frames in the video file.
            CAP_PROP_FOURCC: 4-character code of codec.
        """
        self._cap = ThreadedVideoCapture(src, is_live=True, buffer_size=1,
                                         **kwargs)

    def start(self):
        self._cap.start()

    def stop(self):
        self._cap.stop()

    def read(self):
        return self._cap.read()
