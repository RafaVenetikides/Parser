from sys import argv
from parser.parser import parse
from parser.reader import load_tokens
from itertools import groupby

if __name__ == "__main__":
    all_tokens = load_tokens(f'{argv[1]}')
    all_tokens.sort(key=lambda t: (t.line, t.column))

    for line_no, group in groupby(all_tokens, key=lambda t: t.line):
        token_list = list(group)
        print(f"\n=== AST for line {line_no} ===")
        try:
            ast = parse(token_list.copy())
            print(ast)
            ast.to_graphviz(filename=f"out/graphs/ast_line_{line_no}", format="png")
        except SyntaxError as e:
            print(f"Erro na linha {line_no}: {e}")