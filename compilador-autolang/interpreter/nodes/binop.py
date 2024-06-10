from .base import Node

class BinOp(Node):
    def __init__(self, operator, left, right):
        super().__init__(operator)
        self.left = left
        self.right = right

    def evaluate(self, symbol_table):
        left_result = self.left.evaluate(symbol_table)
        right_result = self.right.evaluate(symbol_table)

        if not (isinstance(left_result, tuple) and isinstance(right_result, tuple)):
            raise ValueError("Expected results to be tuples")

        left_value, left_type = left_result
        right_value, right_type = right_result

        if left_type == 'bool':
            left_value = int(left_value)
        if right_type == 'bool':
            right_value = int(right_value)

        if self.value == '+':
            if left_type == 'int' and right_type == 'int':
                return left_value + right_value, 'int'
            elif left_type == 'string' or right_type == 'string':
                return str(left_value) + str(right_value), 'string'
            elif left_type == 'bool' or right_type == 'bool':
                left_value = int(left_value) if left_type == 'bool' else left_value
                right_value = int(right_value) if right_type == 'bool' else right_value
                return left_value + right_value, 'int'
            else:
                raise TypeError(f"Addition not supported between types {left_type} and {right_type}")
        elif self.value == '-':
            if left_type in {'int', 'bool'} and right_type in {'int', 'bool'}:
                return left_value - right_value, 'int'
            else:
                raise TypeError("Subtraction requires both operands to be integers or booleans coerced to integers.")
        elif self.value == '*':
            if left_type in {'int', 'bool'} and right_type in {'int', 'bool'}:
                return left_value * right_value, 'int'
            else:
                raise TypeError("Multiplication requires both operands to be integers or booleans coerced to integers.")
        elif self.value == '/':
            if left_type in {'int', 'bool'} and right_type in {'int', 'bool'}:
                if right_value == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                return left_value // right_value, 'int'
            else:
                raise TypeError("Division requires both operands to be integers or booleans coerced to integers.")
        elif self.value == '..':
            return str(left_value) + str(right_value), 'string'
        else:
            raise NotImplementedError(f"Operator {self.value} is not implemented")
