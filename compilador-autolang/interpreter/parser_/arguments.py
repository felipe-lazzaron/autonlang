class ArgumentsParser:
    @staticmethod
    def parse_arguments(tokenizer, symbol_table):
        from interpreter.parser_.expression import ExpressionParser

        args = []
        while tokenizer.next.type != "OPERATOR" or tokenizer.next.value != ")":
            if tokenizer.next.type == "NEWLINE":
                tokenizer.select_next()
                continue
            arg = ExpressionParser.parse_expression(tokenizer, symbol_table)
            args.append(arg)
            if tokenizer.next.type == "OPERATOR" and tokenizer.next.value == ",":
                tokenizer.select_next()
        return args
