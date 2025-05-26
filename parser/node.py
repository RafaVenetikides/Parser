class ASTNode:
    def __init__(self, type_, value = None, children = None):
        self.type = type_
        self.value = value
        self.children = children or []

    def __repr__(self, level = 0):
        ret = " " * level + f"{self.type}: {self.value}\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret