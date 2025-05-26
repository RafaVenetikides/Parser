class Token:
    def __init__(self, value, type_, line, column):
        self.value = value
        self.type = type_
        self.line = line
        self.column = column

    def __repr__(self):
        return f"<{self.type} {self.value} at {self.line}:{self.column}>"