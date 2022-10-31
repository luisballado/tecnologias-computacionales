import math

#leer https://ply.readthedocs.io/en/latest/ply.html#lex-example
#leer https://ericknavarro.io/2020/02/10/24-Mi-primer-proyecto-utilizando-PLY/

# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

#token list
tokens = (
    'NAME','NUMBER','DOUBLE','SEN',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN','POW',
    )

# Specification of tokens
# Tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_POW     = r'\^'
t_SEN     = r'seno\(\d+\)'
####################################################################
#Funciones de análisis léxico
####################################################################
    
def t_DOUBLE(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Double value too large %d", t.value)
        t.value = 0
    return t
    
def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules

precedence = ( ('left','PLUS','MINUS'),
               ('left','POW','TIMES','DIVIDE','SEN'),
               ('right','UMINUS'),
            )


####################################################################
#Funciones de análisis sintáctico
####################################################################
# dictionary of names
names = { }
def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    print('ASSIGN')
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print("statement_expr")
    print(t[1])
    
def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    print('EXPRESSION')
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expression_pow(t):
    'expression : expression POW expression'
    t[0] = pow(t[1],t[3])

def p_expression_sen(t):
    'expression : SEN LPAREN expression RPAREN'
    print(t[0])
    print(t[1])
    print(t[2])
    print(t[3])
    t[0] = math.sin(t[2])
    
def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    print('UMINUS')
    print(t[1])
    if t[1] == '-':
        t[0] = -t[2]
    else:
        t[0] == math.sin(t[2])
    
    
def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    print('GROUP')
    t[0] = t[2]
            
        
def p_expression_number(t):
    '''expression : NUMBER
                  | DOUBLE'''
    print('NUMBER')
    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    print('NAME')
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)
