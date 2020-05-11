from .video_input_stream import VideoInputStream
from .threaded_video_capture import ThreadedVideoCapture


class CamVideoInputVideoInputStream(VideoInputStream):
    def __init__(self,
                 src: int,
                 is_live: bool,
                 buffer_size: int):
        if is_live:
            buffer_size = 1
        self._cap = ThreadedVideoCapture(src, is_live, buffer_size)

    def start(self):
        self._cap.start()

    def stop(self):
        self._cap.stop()

    def read(self):
        return self._cap.read()
