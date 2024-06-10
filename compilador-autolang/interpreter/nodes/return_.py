from .base import Node

class Return(Node):
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, symbol_table):
        value, type_ = self.expression.evaluate(symbol_table)
        return value, type_
