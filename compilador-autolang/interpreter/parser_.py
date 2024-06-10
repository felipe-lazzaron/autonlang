from interpreter.tokenizer_ import Tokenizer

class StatementParser:
    @staticmethod
    def parse_statement(tokenizer, symbol_table):
        if tokenizer.next.type == 'KEYWORD':
            if tokenizer.next.value == 'var':
                return StatementParser.parse_var_declaration(tokenizer, symbol_table)
            elif tokenizer.next.value == 'if':
                return StatementParser.parse_if_statement(tokenizer, symbol_table)
            elif tokenizer.next.value == 'while':
                return StatementParser.parse_while_loop(tokenizer, symbol_table)
            elif tokenizer.next.value == 'send':
                return StatementParser.parse_communication(tokenizer, symbol_table)
            elif tokenizer.next.value == 'receive':
                return StatementParser.parse_communication(tokenizer, symbol_table)
            else:
                raise SyntaxError(f"Unexpected keyword: {tokenizer.next.value}")
        elif tokenizer.next.type == 'IDENTIFIER':
            return StatementParser.parse_assignment(tokenizer, symbol_table)
        else:
            raise SyntaxError(f"Unexpected statement type: {tokenizer.next.type}")

    @staticmethod
    def parse_var_declaration(tokenizer, symbol_table):
        tokenizer.select_next()  # Skip 'var'
        identifier = tokenizer.next.value
        tokenizer.select_next()
        if tokenizer.next.value != ':':
            raise SyntaxError("Expected ':' in variable declaration")
        tokenizer.select_next()
        type_ = tokenizer.next.value
        tokenizer.select_next()
        if tokenizer.next.value == '=':
            tokenizer.select_next()
            expression = StatementParser.parse_expression(tokenizer, symbol_table)
        else:
            expression = None
        if tokenizer.next.value != ';':
            raise SyntaxError("Expected ';' at the end of variable declaration")
        tokenizer.select_next()
        return ('var_declaration', identifier, type_, expression)

    @staticmethod
    def parse_assignment(tokenizer, symbol_table):
        identifier = tokenizer.next.value
        tokenizer.select_next()
        if tokenizer.next.value != '=':
            raise SyntaxError("Expected '=' in assignment")
        tokenizer.select_next()
        expression = StatementParser.parse_expression(tokenizer, symbol_table)
        if tokenizer.next.value != ';':
            raise SyntaxError("Expected ';' at the end of assignment")
        tokenizer.select_next()
        return ('assignment', identifier, expression)

    @staticmethod
    def parse_if_statement(tokenizer, symbol_table):
        tokenizer.select_next()  # Skip 'if'
        if tokenizer.next.value != '(':
            raise SyntaxError("Expected '(' after 'if'")
        tokenizer.select_next()
        condition = StatementParser.parse_condition(tokenizer, symbol_table)
        if tokenizer.next.value != ')':
            raise SyntaxError("Expected ')' after 'if' condition")
        tokenizer.select_next()
        if tokenizer.next.value != '{':
            raise SyntaxError("Expected '{' after 'if' condition")
        tokenizer.select_next()
        statements = StatementParser.parse_block(tokenizer, symbol_table)
        if tokenizer.next.value != '}':
            raise SyntaxError("Expected '}' after 'if' block")
        tokenizer.select_next()
        if tokenizer.next.value == 'else':
            tokenizer.select_next()
            if tokenizer.next.value != '{':
                raise SyntaxError("Expected '{' after 'else'")
            tokenizer.select_next()
            else_statements = StatementParser.parse_block(tokenizer, symbol_table)
            if tokenizer.next.value != '}':
                raise SyntaxError("Expected '}' after 'else' block")
            tokenizer.select_next()
            return ('if_statement', condition, statements, else_statements)
        return ('if_statement', condition, statements, None)

    @staticmethod
    def parse_while_loop(tokenizer, symbol_table):
        tokenizer.select_next()  # Skip 'while'
        if tokenizer.next.value != '(':
            raise SyntaxError("Expected '(' after 'while'")
        tokenizer.select_next()
        condition = StatementParser.parse_condition(tokenizer, symbol_table)
        if tokenizer.next.value != ')':
            raise SyntaxError("Expected ')' after 'while' condition")
        tokenizer.select_next()
        if tokenizer.next.value != '{':
            raise SyntaxError("Expected '{' after 'while' condition")
        tokenizer.select_next()
        statements = StatementParser.parse_block(tokenizer, symbol_table)
        if tokenizer.next.value != '}':
            raise SyntaxError("Expected '}' after 'while' block")
        tokenizer.select_next()
        return ('while_loop', condition, statements)

    @staticmethod
    def parse_communication(tokenizer, symbol_table):
        keyword = tokenizer.next.value
        tokenizer.select_next()  # Skip 'send' or 'receive'
        if tokenizer.next.value != '(':
            raise SyntaxError("Expected '(' after 'send' or 'receive'")
        tokenizer.select_next()
        identifier = tokenizer.next.value
        tokenizer.select_next()
        if tokenizer.next.value != ',':
            raise SyntaxError("Expected ',' in 'send' or 'receive'")
        tokenizer.select_next()
        string_literal = tokenizer.next.value
        tokenizer.select_next()
        if tokenizer.next.value != ')':
            raise SyntaxError("Expected ')' after 'send' or 'receive'")
        tokenizer.select_next()
        if tokenizer.next.value != ';':
            raise SyntaxError("Expected ';' after 'send' or 'receive'")
        tokenizer.select_next()
        return (keyword, identifier, string_literal)

    @staticmethod
    def parse_expression(tokenizer, symbol_table):
        # Implementação simplificada para expressão
        term = StatementParser.parse_term(tokenizer, symbol_table)
        while tokenizer.next.type in {'PLUS', 'MINUS'}:
            op = tokenizer.next
            tokenizer.select_next()
            term = ('binop', op.value, term, StatementParser.parse_term(tokenizer, symbol_table))
        return term

    @staticmethod
    def parse_term(tokenizer, symbol_table):
        # Implementação simplificada para termos
        factor = StatementParser.parse_factor(tokenizer, symbol_table)
        while tokenizer.next.type in {'MULT', 'DIV'}:
            op = tokenizer.next
            tokenizer.select_next()
            factor = ('binop', op.value, factor, StatementParser.parse_factor(tokenizer, symbol_table))
        return factor

    @staticmethod
    def parse_factor(tokenizer, symbol_table):
        if tokenizer.next.type == 'NUMBER':
            value = tokenizer.next.value
            tokenizer.select_next()
            return ('number', value)
        elif tokenizer.next.type == 'IDENTIFIER':
            value = tokenizer.next.value
            tokenizer.select_next()
            return ('identifier', value)
        elif tokenizer.next.type == 'STRING_LITERAL':
            value = tokenizer.next.value
            tokenizer.select_next()
            return ('string', value)
        elif tokenizer.next.type == 'SYMBOL' and tokenizer.next.value == '(':
            tokenizer.select_next()
            expr = StatementParser.parse_expression(tokenizer, symbol_table)
            if tokenizer.next.type != 'SYMBOL' or tokenizer.next.value != ')':
                raise SyntaxError("Expected ')'")
            tokenizer.select_next()
            return expr
        else:
            raise SyntaxError("Unexpected token")

    @staticmethod
    def parse_condition(tokenizer, symbol_table):
        left = StatementParser.parse_expression(tokenizer, symbol_table)
        if tokenizer.next.type not in {'EQUALS', 'NEQ', 'LT', 'LTE', 'GT', 'GTE'}:
            raise SyntaxError("Expected comparison operator in condition")
        operator = tokenizer.next.value
        tokenizer.select_next()
        right = StatementParser.parse_expression(tokenizer, symbol_table)
        return ('condition', operator, left, right)

    @staticmethod
    def parse_block(tokenizer, symbol_table):
        statements = []
        while tokenizer.next.type != "EOF" and tokenizer.next.type != 'SYMBOL':
            statements.append(StatementParser.parse_statement(tokenizer, symbol_table))
        return statements
