from .base import Node

class RelOp(Node):
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

        if left_type == 'bool' and right_type == 'int':
            left_value = int(left_value)
        elif right_type == 'bool' and left_type == 'int':
            right_value = int(right_value)
        elif left_type != right_type:
            raise TypeError("Comparison between different types: {} and {}".format(left_type, right_type))

        if self.value == '==':
            result = left_value == right_value
        elif self.value == '!=':
            result = left_value != right_value
        elif self.value == '<':
            result = left_value < right_value
        elif self.value == '>':
            result = left_value > right_value
        elif self.value == '<=':
            result = left_value <= right_value
        elif self.value == '>=':
            result = left_value >= right_value
        else:
            raise NotImplementedError("Relational operation '{}' not implemented".format(self.value))

        return result, 'bool'
