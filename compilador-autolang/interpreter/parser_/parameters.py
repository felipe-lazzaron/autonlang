from interpreter.nodes.parameter import Parameter

class ParametersParser:
    @staticmethod
    def parse_parameters(tokenizer, symbol_table):
        params = []
        while tokenizer.next.type == "IDENTIFIER":
            params.append(Parameter(tokenizer.next.value))
            tokenizer.select_next()
            if tokenizer.next.type == "OPERATOR" and tokenizer.next.value == ",":
                tokenizer.select_next()
        return params
