from interpreter.nodes.base import Node

class Argument(Node):
    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table):
        return self.value.evaluate(symbol_table)
