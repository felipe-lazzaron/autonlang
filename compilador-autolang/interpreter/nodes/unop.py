from .base import Node

class UnOp(Node):
    def __init__(self, operator, operand):
        super().__init__(operator)
        self.operand = operand

    def evaluate(self, symbol_table):
        operand_result = self.operand.evaluate(symbol_table)
        if not isinstance(operand_result, tuple):
            raise TypeError("Operand did not return a tuple.")
        operand_value, operand_type = operand_result

        if operand_type != 'int':
            raise TypeError("Unary operations can only be applied to integers.")

        if self.value == '-':
            return -operand_value, 'int'
        elif self.value == '+':
            return operand_value, 'int'
        else:
            raise NotImplementedError(f"Unary operation '{self.value}' not implemented.")
