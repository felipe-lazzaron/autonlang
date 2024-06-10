class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __str__(self):
        return f"Token(type={self.type}, value={self.value})"

    __repr__ = __str__


class Tokenizer:
    KEYWORDS = {'var', 'if', 'while', 'send', 'receive'}

    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next = None

    def select_next(self):
        while self.position < len(self.source) and self.source[self.position] in {' ', '\t', '\n'}:
            self.position += 1

        if self.position < len(self.source):
            current_char = self.source[self.position]

            if current_char.isdigit():
                start = self.position
                while self.position < len(self.source) and self.source[self.position].isdigit():
                    self.position += 1
                self.next = Token("NUMBER", int(self.source[start:self.position]))
                return
            elif current_char.isalpha() or current_char == '_':
                start = self.position
                while self.position < len(self.source) and (self.source[self.position].isalnum() or self.source[self.position] == '_'):
                    self.position += 1
                word = self.source[start:self.position]
                if word in Tokenizer.KEYWORDS:
                    self.next = Token("KEYWORD", word)
                else:
                    self.next = Token("IDENTIFIER", word)
                return
            elif current_char == '"':
                self.position += 1
                start = self.position
                while self.position < len(self.source) and self.source[self.position] != '"':
                    self.position += 1
                self.next = Token("STRING_LITERAL", self.source[start:self.position])
                self.position += 1
                return
            elif current_char in {'+', '-', '*', '/'}:
                self.next = Token("OPERATOR", current_char)
                self.position += 1
                return
            elif current_char in {'(', ')', '{', '}', ';', ',', ':', '='}:
                self.next = Token("SYMBOL", current_char)
                self.position += 1
                return
            elif current_char == '>' or current_char == '<':
                start = self.position
                self.position += 1
                if self.position < len(self.source) and self.source[self.position] == '=':
                    self.position += 1
                self.next = Token("OPERATOR", self.source[start:self.position])
                return
            elif current_char == '=' or current_char == '!':
                start = self.position
                self.position += 1
                if self.position < len(self.source) and self.source[self.position] == '=':
                    self.position += 1
                self.next = Token("OPERATOR", self.source[start:self.position])
                return
            else:
                raise ValueError(f"Invalid character: {current_char}")
        else:
            self.next = Token("EOF", None)
