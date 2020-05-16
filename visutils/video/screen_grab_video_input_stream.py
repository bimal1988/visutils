import logging
from queue import Empty, Queue
from threading import Thread

import numpy as np
from mss import mss

from .video_input_stream import VideoInputStream


class ScreenGrabVideoInputStream(VideoInputStream):
    def __init__(self, monitor_idx=1, is_live=True, buffer_size=128):
        self._sct = mss()
        self._monitor = None
        try:
            self._monitor = self._sct.monitors[monitor_idx]
        except Exception as e:
            logging.error(str(e))

        self._is_live = is_live
        self._buffer = Queue(maxsize=buffer_size)
        self._thread = Thread(target=self._update, args=())
        self._thread.daemon = True
        self._stopped = False

    def start(self):
        self._thread.start()

    def _update(self):
        while not self._stopped:
            frame = np.array(self._sct.grab(self._monitor)) # noqa

            if frame is None:
                self._shutdown()
                break

            if self._is_live:
                self._clear_buffer()

            self._buffer.put(frame)

        self._sct.close()

    def stop(self):
        self._shutdown()
        self._thread.join()

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

    def read(self):
        return self._buffer.get()
