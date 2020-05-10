from threading import Thread
from queue import Queue, Empty
import cv2
from visutils.common import Timer


class ThreadedVideoCapture:
    def __init__(self, source, is_realtime, buffer_size):
        self._cap = cv2.VideoCapture(source)
        self._is_realtime = is_realtime
        self._buffer = Queue(maxsize=buffer_size)
        self._thread = Thread(target=self._update, args=())
        self._thread.daemon = True
        self._stopped = False
        self._timer = Timer()

    def start(self):
        self._thread.start()
        self._timer.start()

    def _update(self):
        while not self._stopped:
            (success, frame) = self._cap.read()
            self._timer.tick()
            if not success:
                self._shutdown()
                break

            if self._is_realtime:
                self._clear_buffer()

            self._buffer.put(frame)

        self._cap.release()

    def read(self):
        return self._buffer.get()

    def _shutdown(self):
        self._stopped = True
        self._clear_buffer()
        self._buffer.put(None)

    def _clear_buffer(self):
        while not self._buffer.empty():
            try:
                self._buffer.get_nowait()
            except Empty:
                pass

    def stop(self):
        self._timer.stop()
        print("Inside: ", self._timer.ticks_per_second())
        self._shutdown()
        self._thread.join()
