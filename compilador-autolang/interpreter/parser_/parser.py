from interpreter.tokenizer_ import Tokenizer
from .statement import StatementParser
from .block import BlockParser
from .expression import ExpressionParser

class Parser:

    @staticmethod
    def parse_expression(tokenizer, symbol_table):
        return ExpressionParser.parse_expression(tokenizer, symbol_table)

    @staticmethod
    def parse_block(tokenizer, symbol_table):
        return BlockParser.parse_block(tokenizer, symbol_table)

    @staticmethod
    def parse_statement(tokenizer, symbol_table):
        return StatementParser.parse_statement(tokenizer, symbol_table)

    @staticmethod
    def run(code, symbol_table):
        tokenizer = Tokenizer(code)
        tokenizer.select_next()
        result = Parser.parse_block(tokenizer, symbol_table)
        if tokenizer.next.type != "EOF":
            raise SyntaxError("Unexpected token at the end of parsing")
        return result
