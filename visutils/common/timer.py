import datetime


class Timer:
    def __init__(self):
        self._start = None
        self._end = None
        self._numTicks = 0

    def start(self):
        self._start = datetime.datetime.now()

    def stop(self):
        self._end = datetime.datetime.now()

    def tick(self):
        self._numTicks += 1

    def elapsed(self):
        return (self._end - self._start).total_seconds()

    def ticks_per_second(self):
        return self._numTicks / self.elapsed()
