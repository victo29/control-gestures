from abc import ABC, abstractmethod

class HandDetector(ABC):

    @abstractmethod
    def find_hands(self, img):
        raise NotImplementedError('"find_hands" must be implemented')
