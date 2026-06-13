from abc import ABC, abstractmethod

class Memory(ABC):

    @abstractmethod
    def add(self, role, content):
        pass

    @abstractmethod
    def get_context(self):
        pass