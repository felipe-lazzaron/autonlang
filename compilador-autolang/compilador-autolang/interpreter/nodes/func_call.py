from ..symbol_table import SymbolTable
from .base import Node

class FuncCall(Node):
    def __init__(self, func_name, args):
        self.func_name = func_name
        self.args = args

    def evaluate(self, symbol_table):
        if self.func_name == 'read':
            return FuncCall.read()

        func = symbol_table.get_function(self.func_name)
        if func is None:
            raise ValueError(f"Function '{self.func_name}' not found")

        local_symbol_table = SymbolTable()
        for param, arg in zip(func.params, self.args):
            value, type_ = arg.evaluate(symbol_table)
            local_symbol_table.set_variable(param.value, value, type_)  # Ensure param is evaluated correctly

        result = func.body.evaluate(local_symbol_table)
        return result  # Ensure we return the result properly

    @staticmethod
    def read():
        try:
            user_input = input("")
            value = int(user_input)
            return value, "int"
        except ValueError:
            raise ValueError("Invalid input for read(), expected an integer.")
