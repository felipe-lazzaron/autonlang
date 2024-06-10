from interpreter.nodes.base import Node

class Parameter(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, symbol_table):
        # O evaluate para um parâmetro pode simplesmente retornar seu valor
        return self.value, "parameter"
