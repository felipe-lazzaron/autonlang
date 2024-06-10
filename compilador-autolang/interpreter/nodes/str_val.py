from .base import Node

class StrVal(Node):
    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table=None):
        return self.value, "string"
