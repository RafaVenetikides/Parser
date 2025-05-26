from node import ASTNode
from reader import load_tokens
from table import ll1_table
from parser_token import Token

def parse(tokens):
    stack = ['$', 'S']
    tokens.append(Token('$', '$', -1, -1))

    pos = 0
    current_token = tokens[pos]

    root = ASTNode('S')

    node_stack = [root]

    while stack:
        top = stack.pop()
        current_node = node_stack.pop()

        if top == '$' and current_token.type == '$':
            print("Sucessfully pased line")
            return root

        elif top in ['OPEN_PAREN', 'CLOSE_PAREN', 'NUMBER', 'MEM', 'OPERATOR', 'RES', 'IF', 'THEN', 'ELSE', 'FOR', 'DO']:
            if top == current_token.type:
                leaf = ASTNode('TOKEN', current_token.value)
                current_node.children.append(leaf)
                pos += 1
                current_token = tokens[pos]
            else:
                raise SyntaxError(f"Syntax error: expected {top}, found {current_token.type} (current: {current_token.value})")

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
            raise SyntaxError(f"Syntax Error: expected {top}, found {current_token.type} (current: {current_token.value})")

    return root
