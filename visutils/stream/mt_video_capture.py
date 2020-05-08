from threading import Thread
import cv2
from visutils.common import Timer


class MTVideoCapture:
    def __init__(self, source):
        self._cap = cv2.VideoCapture(source)
        self._frame = None
        self._thread = Thread(target=self._update, args=())
        self._thread.daemon = True
        self._stopped = False
        self._timer = Timer()
        print('threaded')

    def start(self):
        self._thread.start()

    def _update(self):
        self._timer.start()
        cnt = 0
        while not self._stopped:
            (success, frame) = self._cap.read()
            self._timer.tick()
            cnt += 1
            if not success:
                self._stopped = True
            self._frame = frame
            if cnt == 350:
                self._timer.stop()
                print("Inside: ", self._timer.ticks_per_second())

    def read(self):
        return self._frame

    def stop(self):
        self._stopped = True
