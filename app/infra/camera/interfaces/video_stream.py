from abc import ABC, abstractmethod

class VideoStream(ABC):

    @abstractmethod
    def is_open(self):
        raise NotImplementedError('"is_open" must be implemented')

    @abstractmethod
    def read(self):
        raise NotImplementedError('"read" must be implemented')

    @abstractmethod
    def release(self):
        raise NotImplementedError('"release" must be implemented')
