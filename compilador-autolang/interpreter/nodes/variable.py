from .base import Node

class Variable(Node):
    def __init__(self, identifier):
        super().__init__(identifier)

    def evaluate(self, symbol_table=None, default=None):
        if symbol_table is not None:
            if not symbol_table.is_declared(self.value):
                raise NameError(f"Variable '{self.value}' not declared")
            variable = symbol_table.get_variable(self.value)
            if variable is None:
                raise NameError(f"Variable '{self.value}' not found")
            value, type_ = variable
            return value, type_
        return default, None
