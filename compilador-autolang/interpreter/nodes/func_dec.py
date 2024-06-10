from ..symbol_table import SymbolTable
from .base import Node

class FuncDec(Node):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def evaluate(self, symbol_table):
        symbol_table.set_function(self.name, self)
