from .base import Node

class IfStatement(Node):
    def __init__(self, condition, then_body, else_body=None):
        super().__init__(None)
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body

    def evaluate(self, symbol_table):
        if self.condition.evaluate(symbol_table)[0]:  # Certifica que avalia como booleano
            self.then_body.evaluate(symbol_table)
        elif self.else_body:
            self.else_body.evaluate(symbol_table)
