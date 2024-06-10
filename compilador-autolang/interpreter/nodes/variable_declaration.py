from .base import Node

class VariableDeclaration(Node):
    def __init__(self, identifier):
        super().__init__(identifier)

    def evaluate(self, symbol_table):
        symbol_table.set_variable(self.value, None, None)
