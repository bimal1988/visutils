from abc import ABCMeta, abstractmethod


class VideoInputStream(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError

    @abstractmethod
    def read(self):
        raise NotImplementedError
