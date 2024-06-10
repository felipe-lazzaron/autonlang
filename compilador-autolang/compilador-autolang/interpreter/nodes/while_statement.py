from .base import Node

class WhileStatement(Node):
    def __init__(self, condition, body):
        super().__init__(None)
        self.condition = condition
        self.body = body

    def evaluate(self, symbol_table):
        while True:
            condition_result = self.condition.evaluate(symbol_table)[0]  # Assume que o resultado da condição é um tuple (value, type)
            if not condition_result:  # Se a condição for falsa, interrompe o loop
                break
            self.body.evaluate(symbol_table)  # Executa o corpo do loop
