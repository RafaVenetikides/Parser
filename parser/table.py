ll1_table = {
    ('S', 'OPEN_PAREN'): ['Expr'],
    ('Expr', 'OPEN_PAREN'): ['OPEN_PAREN', 'RPNExpr', 'CLOSE_PAREN'],

    ('RPNExpr', 'OPEN_PAREN'): ['Operand', 'RPNExprPrime'],
    ('RPNExpr', 'NUMBER'): ['Operand', 'RPNExprPrime'],
    ('RPNExpr', 'MEM'): ['MEM_Operand'],

    ('RPNExprPrime', 'OPEN_PAREN'): ['Operand', 'Operator'],
    ('RPNExprPrime', 'NUMBER'): ['Operand', 'Operator'],
    ('RPNExprPrime', 'MEM'): ['OperatorUnary'],
    ('RPNExprPrime', 'RES'): ['OperatorUnary'],
    ('RPNExprPrime', 'IF'): ['OperatorUnary'],
    ('RPNExprPrime', 'THEN'): ['OperatorUnary'],
    ('RPNExprPrime', 'ELSE'): ['OperatorUnary'],
    ('RPNExprPrime', 'FOR'): ['OperatorUnary'],
    ('RPNExprPrime', 'DO'): ['OperatorUnary'],

    ('Operand', 'OPEN_PAREN'): ['Expr'],
    ('Operand', 'NUMBER'): ['NUMBER'],

    ('Operator', 'OPERATOR'): ['OPERATOR'],
    ('OperatorUnary', 'MEM'): ['MEM'],
    ('OperatorUnary', 'RES'): ['RES'],
    ('OperatorUnary', 'IF'): ['IF'],
    ('OperatorUnary', 'THEN'): ['THEN'],
    ('OperatorUnary', 'ELSE'): ['ELSE'],
    ('OperatorUnary', 'FOR'): ['FOR'],
    ('OperatorUnary', 'DO'): ['DO'],

    ('MEM_Operand', 'MEM'): ['MEM'],
}