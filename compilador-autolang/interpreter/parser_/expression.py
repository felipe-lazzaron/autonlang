from interpreter.nodes.variable import Variable
from interpreter.nodes.int_val import IntVal
from interpreter.nodes.str_val import StrVal
from interpreter.nodes.unop import UnOp
from interpreter.nodes.binop import BinOp
from interpreter.nodes.func_call import FuncCall
from interpreter.nodes.not_op import NotOp
from interpreter.nodes.rel_op import RelOp
from interpreter.nodes.bool_op import BoolOp

class ExpressionParser:
    @staticmethod
    def parse_expression(tokenizer, symbol_table):
        return ExpressionParser.parse_boolean_expression(tokenizer, symbol_table)

    @staticmethod
    def parse_boolean_expression(tokenizer, symbol_table):
        result = ExpressionParser.parse_relational_expression(tokenizer, symbol_table)
        while tokenizer.next.type == "KEYWORD" and tokenizer.next.value in ('and', 'or'):
            operator = tokenizer.next.value
            tokenizer.select_next()
            right = ExpressionParser.parse_relational_expression(tokenizer, symbol_table)
            result = BoolOp(operator, left=result, right=right)
        return result

    @staticmethod
    def parse_relational_expression(tokenizer, symbol_table):
        result = ExpressionParser.parse_arithmetic_expression(tokenizer, symbol_table)
        while tokenizer.next.type == "OPERATOR" and tokenizer.next.value in ('==', '!=', '<', '>', '<=', '>='):
            operator = tokenizer.next.value
            tokenizer.select_next()
            right = ExpressionParser.parse_arithmetic_expression(tokenizer, symbol_table)
            result = RelOp(operator, left=result, right=right)
        return result

    @staticmethod
    def parse_arithmetic_expression(tokenizer, symbol_table):
        result = ExpressionParser.parse_term(tokenizer, symbol_table)
        while tokenizer.next.type == "OPERATOR" and tokenizer.next.value in ('+', '-', '..'):
            operator = tokenizer.next.value
            tokenizer.select_next()
            right = ExpressionParser.parse_term(tokenizer, symbol_table)
            result = BinOp(operator, left=result, right=right)
        return result

    @staticmethod
    def parse_term(tokenizer, symbol_table):
        result = ExpressionParser.parse_factor(tokenizer, symbol_table)
        while tokenizer.next.type == "OPERATOR" and tokenizer.next.value in ('*', '/'):
            operator = tokenizer.next.value
            tokenizer.select_next()
            right = ExpressionParser.parse_factor(tokenizer, symbol_table)
            result = BinOp(operator, left=result, right=right)
        return result

    @staticmethod
    def parse_factor(tokenizer, symbol_table):
        token = tokenizer.next
        if token.type == "NUMBER":
            tokenizer.select_next()
            return IntVal(token.value)
        elif token.type == "STRING":
            if token.value and token.value[-1] != '"' and '"' in token.value:
                raise SyntaxError("String missing closing quote")
            tokenizer.select_next()
            if tokenizer.next.type == "EOF":
                raise SyntaxError("Unexpected end of file")
            return StrVal(token.value)
        elif token.type == "KEYWORD" and token.value == 'read':
            tokenizer.select_next()
            if tokenizer.next.type == "OPERATOR" and tokenizer.next.value == '(':
                tokenizer.select_next()
                if tokenizer.next.type == "OPERATOR" and tokenizer.next.value == ')':
                    tokenizer.select_next()
                    return FuncCall('read', [])
                else:
                    raise SyntaxError("Expected ')' after 'read'")
        elif token.type == "KEYWORD" and token.value == 'not':
            tokenizer.select_next()
            operand = ExpressionParser.parse_factor(tokenizer, symbol_table)
            return NotOp(operand)
        elif token.type == "OPERATOR" and token.value in ('-', '+'):
            op = token.value
            tokenizer.select_next()
            operand = ExpressionParser.parse_factor(tokenizer, symbol_table)
            return UnOp(op, operand)
        elif token.type == "OPERATOR" and token.value == '(':
            tokenizer.select_next()
            result = ExpressionParser.parse_expression(tokenizer, symbol_table)
            if tokenizer.next.type != "OPERATOR" or tokenizer.next.value != ')':
                raise SyntaxError("Expected ')' after expression")
            tokenizer.select_next()
            return result
        elif token.type == "IDENTIFIER":
            identifier = token.value
            tokenizer.select_next()
            if tokenizer.next.type == "OPERATOR" and tokenizer.next.value == "(":
                tokenizer.select_next()
                from interpreter.parser_.arguments import ArgumentsParser
                args = ArgumentsParser.parse_arguments(tokenizer, symbol_table)
                if tokenizer.next.type != "OPERATOR" or tokenizer.next.value != ")":
                    raise SyntaxError("Expected ')' after function arguments")
                tokenizer.select_next()
                return FuncCall(identifier, args)
            return Variable(identifier)
        elif token.type == "EOF":
            raise SyntaxError("Unexpected end of file")
        else:
            raise SyntaxError(f"Unexpected token: {token.type}, {token.value}")
