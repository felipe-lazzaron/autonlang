from .base import Node
from interpreter.nodes.return_ import Return

# interpreter/nodes/block.py
class Block:
    def __init__(self, children=None):
        self.statements = children or []
    
    def add_statement(self, statement):
        self.statements.append(statement)
    
    def evaluate(self, symbol_table):
        for child in self.statements:
            result = child.evaluate(symbol_table)
            if isinstance(result, tuple):  # Check if the result is a return statement
                return result
