from visutils.stream import VideoInputStream
from mss import mss


class ScreenGrabVideoInputStream(VideoInputStream):
    def __init__(self, monitor_idx=1, ):
        self._sct = mss()
        monitor = None
        if monitor_idx >= 0:
            try:
                monitor = self._sct.monitors[monitor_idx]
            except Exception as e:
                print(str(e))
                monitor = None
        else:
            raise ValueError(
                "[VisUtils:ERROR] :: `monitor` value cannot be negative!"
            )

    def start(self):
        pass

    def stop(self):
        pass

    def read(self):
        pass
