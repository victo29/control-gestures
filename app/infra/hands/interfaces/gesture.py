from abc import ABC, abstractmethod

class GestureRecognizer(ABC):

    @abstractmethod
    def get_gestures(self, hand):
        raise NotImplementedError('"get_gesture" not implemented error')
