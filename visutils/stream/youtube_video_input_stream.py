from .stream import Stream
from .threaded_video_capture import ThreadedVideoCapture
import pafy


class YoutubeVideoInputStream(Stream):
    def __init__(self,
                 src: str,
                 is_live: bool,
                 buffer_size: int):
        src = pafy.new(src)
        best_stream = src.getbestvideo(preftype='webm')
        self._cap = ThreadedVideoCapture(best_stream.url,
                                         is_live=is_live,
                                         buffer_size=buffer_size)

    def start(self):
        self._cap.start()

    def stop(self):
        self._cap.stop()

    def read(self):
        return self._cap.read()
