from .base import Node

class NotOp(Node):
    def __init__(self, child):
        super().__init__('not')
        self.child = child

    def evaluate(self, symbol_table):
        child_result = self.child.evaluate(symbol_table)
        if not isinstance(child_result, tuple):
            raise TypeError("Child did not return a tuple.")
        child_value, child_type = child_result
        if child_type != 'bool':
            raise TypeError("NOT operation requires a boolean operand.")
        return not child_value, 'bool'
