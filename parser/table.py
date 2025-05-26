ll1_table = {
    ('S', 'OPEN_PAREN'): ['Expr'],

    ('Expr', 'OPEN_PAREN'): ['OPEN_PAREN', 'RPNExpr', 'CLOSE_PAREN'],

    ('RPNExpr', 'OPEN_PAREN'): ['Operand', 'RPNExprPrime'],
    ('RPNExpr', 'NUMBER'): ['Operand', 'RPNExprPrime'],
    ('RPNExpr', 'MEM'): ['Operand', 'RPNExprPrime'],

    ('RPNExprPrime', 'OPEN_PAREN'): ['Operand', 'Operator'],
    ('RPNExprPrime', 'NUMBER'): ['Operand', 'Operator'],
    ('RPNExprPrime', 'MEM'): ['Operand', 'Operator'],
    ('RPNExprPrime', 'RES'): ['OperatorUnary'],
    ('RPNExprPrime', 'IF'): ['OperatorUnary'],
    ('RPNExprPrime', 'THEN'): ['OperatorUnary'],
    ('RPNExprPrime', 'ELSE'): ['OperatorUnary'],
    ('RPNExprPrime', 'FOR'): ['OperatorUnary'],
    ('RPNExprPrime', 'DO'): ['OperatorUnary'],

    ('Operand', 'OPEN_PAREN'): ['Expr'],
    ('Operand', 'NUMBER'): ['NUMBER'],
    ('Operand', 'MEM'): ['MEM'],

    ('Operator', 'OPERATOR'): ['OPERATOR'],
    ('OperatorUnary', 'RES'): ['RES'],
    ('OperatorUnary', 'MEM'): ['MEM'],
    ('OperatorUnary', 'IF'): ['IF'],
    ('OperatorUnary', 'THEN'): ['THEN'],
    ('OperatorUnary', 'ELSE'): ['ELSE'],
    ('OperatorUnary', 'FOR'): ['FOR'],
    ('OperatorUnary', 'DO'): ['DO'],
    ('RPNExprPrime','CLOSE_PAREN'): [],
    ('RPNExprPrime','$'): [],
}