from .node import ASTNode
from .table import ll1_table
from .parser_token import Token

def parse(tokens):
    stack = ['$', 'S']
    tokens.append(Token('$', '$', -1, -1))

    pos = 0
    current_token = tokens[pos]

    root = ASTNode('S')
    node_stack = [root]

    TERMINALS = {
        'OPEN_PAREN', 'CLOSE_PAREN', 'NUMBER',
        'MEM', 'OPERATOR', 'RES', 'IF', 'THEN',
        'ELSE', 'FOR', 'DO'
    }

    while stack:
        top = stack.pop()

        if top == '$' and current_token.type == '$':
            print("Successfully parsed line")
            return root

        if not node_stack:
            raise SyntaxError(
                f"Internal parser error: no AST node to attach symbol {top}"
            )
        current_node = node_stack.pop()

        if top in TERMINALS:
            if top == current_token.type:
                leaf = ASTNode(top, current_token.value)
                current_node.children.append(leaf)
                pos += 1
                current_token = tokens[pos]
            else:
                raise SyntaxError(
                    f"Syntax error: expected {top}, found {current_token.type} "
                    f"(value={current_token.value})"
                )

        elif (top, current_token.type) in ll1_table:
            production = ll1_table[(top, current_token.type)]
            children = []
            for symbol in reversed(production):
                stack.append(symbol)
                child = ASTNode(symbol)
                node_stack.append(child)
                children.insert(0, child)
            current_node.children.extend(children)

        else:
            raise SyntaxError(
                f"Syntax error: no rule for ({top}, {current_token.type}) "
                f"(value={current_token.value})"
            )

    raise SyntaxError("Syntax error: incomplete parse, input not fully consumed")