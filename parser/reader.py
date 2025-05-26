import json
from parser.parser_token import Token

def load_tokens(path):
    with open(path, encoding='utf-8') as f:
        items = json.load(f)
    return [
        Token(d['value'], d['type'], d['line'], d['column'])
        for d in items
    ]