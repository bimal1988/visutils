from multiprocessing import Process, Queue
import cv2

from multiprocessing import Process, Manager
from multiprocessing.managers import BaseManager
from common import Timer


class SimpleClass(object):
    def __init__(self):
        self.var = 0

    def set(self, value):
        self.var = value

    def get(self):
        return self.var


class MPVideoCapture:
    def __init__(self, source):
        BaseManager.register('SimpleClass', SimpleClass)
        manager = BaseManager()
        manager.start()
        self._inst = manager.SimpleClass()

        self._source = source
        self._q = Queue(maxsize=1)
        self._process = Process(target=self._update, args=(self._inst,))
        self._process.daemon = True
        self._stopped = False

    def start(self):
        self._process.start()

    def _update(self, inst):
        timer = Timer()
        cap = cv2.VideoCapture(self._source)
        timer.start()
        cnt = 0
        while not self._stopped:
            (success, frame) = cap.read()
            timer.tick()
            cnt += 1
            if not success:
                cap.release()
            try:
                self._q.get_nowait()
            except:
                pass
            self._q.put(frame)
            # inst.set(frame)
            if cnt == 350:
                timer.stop()
                print("inside: ", timer.ticks_per_second())

    def read(self):
        return self._q.get()
        # return self._inst.get()

    def stop(self):
        self._stopped = True
