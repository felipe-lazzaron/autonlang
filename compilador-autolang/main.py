from interpreter.tokenizer_ import Tokenizer
from interpreter.symbol_table import SymbolTable
from interpreter.parser_ import Parser

def main():
    import sys
    args = sys.argv[1:]
    file_name = args[0] if args else r'.\compilador-autolang\exemplo.autolang'

    with open(file_name, 'r') as file:
        code = file.read()

    symbol_table = SymbolTable()
    ast = Parser.run(code, symbol_table)

    if not isinstance(ast, list):
        raise TypeError("AST is not a list")

    for statement in ast:
        evaluate(statement, symbol_table)

def evaluate(node, symbol_table):
    node_type = node[0]
    if node_type == 'var_declaration':
        _, identifier, type_, expression = node
        value = evaluate(expression, symbol_table) if expression else None
        symbol_table.set_variable(identifier, value, type_)
    elif node_type == 'assignment':
        _, identifier, expression = node
        value = evaluate(expression, symbol_table)
        symbol_table.set_variable(identifier, value, None)
    elif node_type == 'if_statement':
        _, condition, statements, else_statements = node
        if evaluate(condition, symbol_table):
            for stmt in statements:
                evaluate(stmt, symbol_table)
        elif else_statements:
            for stmt in else_statements:
                evaluate(stmt, symbol_table)
    elif node_type == 'while_loop':
        _, condition, statements = node
        while evaluate(condition, symbol_table):
            for stmt in statements:
                evaluate(stmt, symbol_table)
    elif node_type in {'send', 'receive'}:
        _, identifier, string_literal = node
        print(f"{node_type} {identifier}: {string_literal}")
    elif node_type == 'condition':
        _, operator, left, right = node
        left_val = evaluate(left, symbol_table)
        right_val = evaluate(right, symbol_table)
        if operator == '==':
            return left_val == right_val
        elif operator == '!=':
            return left_val != right_val
        elif operator == '<':
            return left_val < right_val
        elif operator == '<=':
            return left_val <= right_val
        elif operator == '>':
            return left_val > right_val
        elif operator == '>=':
            return left_val >= right_val
    elif node_type == 'number':
        return node[1]
    elif node_type == 'identifier':
        return symbol_table.get_variable(node[1])[0]
    elif node_type == 'string':
        return node[1]
    elif node_type == 'binop':
        _, operator, left, right = node
        left_val = evaluate(left, symbol_table)
        right_val = evaluate(right, symbol_table)
        if operator == '+':
            return left_val + right_val
        elif operator == '-':
            return left_val - right_val
        elif operator == '*':
            return left_val * right_val
        elif operator == '/':
            return left_val / right_val
    else:
        raise ValueError(f"Unknown node type: {node_type}")

if __name__ == "__main__":
    main()
