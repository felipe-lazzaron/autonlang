# interpreter/parser_/block.py
from .statement import StatementParser

class BlockParser:
    @staticmethod
    def parse_block(tokenizer, symbol_table):
        statements = []
        while tokenizer.next.type != "EOF" and tokenizer.next.type != 'SYMBOL':
            statements.append(StatementParser.parse_statement(tokenizer, symbol_table))
        return statements
