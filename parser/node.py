from graphviz import Digraph

class ASTNode:
    def __init__(self, type_, value=None, children=None):
        self.type = type_
        self.value = value
        self.children = children or []

    def __repr__(self):
        return self._build_repr()

    def _build_repr(self, prefix='', is_tail=True):
        lines = []
        node_label = f"{self.type}: {self.value}" if self.value is not None else f"{self.type}"
        lines.append(prefix + ('└── ' if is_tail else '├── ') + node_label)
        for i, child in enumerate(self.children):
            next_prefix = prefix + ('    ' if is_tail else '│   ')
            is_last = i == (len(self.children) - 1)
            lines.append(child._build_repr(next_prefix, is_last))
        return '\n'.join(lines)

    def to_graphviz(self, filename="ast", format="png"):
        dot = Digraph(comment="Abstract Syntax Tree", format=format)
        self._add_to_graph(dot)
        dot.render(filename, view=False)
        print(f"AST image saved to {filename}.{format}")

    def _add_to_graph(self, dot, parent_id=None):
        node_id = str(id(self))
        label = f"{self.type}\n{self.value}" if self.value else self.type
        dot.node(node_id, label)
        if parent_id:
            dot.edge(parent_id, node_id)
        for child in self.children:
            child._add_to_graph(dot, node_id)