from .stream import Stream
from .threaded_video_capture import ThreadedVideoCapture


class CamVideoStream(Stream):
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
