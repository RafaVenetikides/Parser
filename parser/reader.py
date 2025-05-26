import json

from parser.parser_token import Token


def load_tokens(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [Token(tok['value'], tok['type'], tok['line'], tok['column']) for tok in data]