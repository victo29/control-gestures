from abc import abstractmethod, ABC

class GestureActions(ABC):

    @abstractmethod
    def handle(self, gesture):
        raise NotImplementedError('"handle" must be implemented')
