from .base import Node

class Assignment(Node):
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

    def evaluate(self, symbol_table):
        value, type_ = self.expression.evaluate(symbol_table)
        symbol_table.set_variable(self.identifier, value, type_)
