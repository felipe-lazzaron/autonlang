from .base import Node

class PrintStatement(Node):
    def __init__(self, value, children=None):
        super().__init__(value)
        self.children = children

    def evaluate(self, symbol_table):
        expr_value, expr_type = self.children[0].evaluate(symbol_table)
        if expr_type == 'bool':
            expr_value = int(expr_value)
        print(expr_value)
        return None
