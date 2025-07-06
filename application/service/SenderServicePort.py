from abc import ABC, abstractmethod


class SenderServicePort(ABC):

    @abstractmethod
    def send(self): pass