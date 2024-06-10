class SymbolTable:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.declared_variables = set()

    def set_variable(self, name, value, type_):
        self.variables[name] = (value, type_)
        self.declared_variables.add(name)

    def get_variable(self, name):
        return self.variables.get(name)

    def set_function(self, name, func):
        self.functions[name] = func

    def get_function(self, name):
        return self.functions.get(name)

    def is_declared(self, name):
        return name in self.declared_variables or name in self.functions
