from .base import Node

class BoolOp(Node):
    def __init__(self, operator, left, right):
        super().__init__(operator)
        self.left = left
        self.right = right

    def evaluate(self, symbol_table):
        left_result = self.left.evaluate(symbol_table)
        right_result = self.right.evaluate(symbol_table)

        if not isinstance(left_result, tuple) or not isinstance(right_result, tuple):
            raise TypeError("Evaluation did not return (value, type)")

        left_value, left_type = left_result
        right_value, right_type = right_result

        if left_type != 'bool' or right_type != 'bool':
            raise TypeError("Boolean operations require both operands to be 'bool', got {} and {}".format(left_type, right_type))

        result = None
        if self.value == 'and':
            result = left_value and right_value
        elif self.value == 'or':
            result = left_value or right_value
        else:
            raise NotImplementedError("Boolean operation '{}' not implemented".format(self.value))

        return result, 'bool'
