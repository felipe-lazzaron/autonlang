from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def evaluate(self, symbol_table=None):
        pass
