from .video_input_stream import VideoInputStream
from .threaded_video_capture import ThreadedVideoCapture


class FileVideoInputVideoInputStream(VideoInputStream):
    def __init__(self,
                 src: str,
                 buffer_size: int):
        self._cap = ThreadedVideoCapture(src, is_live=False, buffer_size=buffer_size)

    def start(self):
        self._cap.start()

    def stop(self):
        self._cap.stop()

    def read(self):
        return self._cap.read()
