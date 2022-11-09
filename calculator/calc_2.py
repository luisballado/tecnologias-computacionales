
import math

#MODULARIDAD ALTA COHESION DEBIL ACOPLAMIENTO
#HERRAMIENTA
#AUTOMATICO
#SERIALIZACION DE OBJETOS guardar el estado de un objeto en disco
#Objeto vive en tiempo de ejecucion
#Clase vive en tiempo de asignacion

# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

#token list
tokens = (
    'NAME','NUMBER','DOUBLE',
    'PLUS','MINUS',
    'TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN','POW','MOD'
)

# Specification of tokens
# Tokens
t_PLUS         = r'\+'
t_MINUS        = r'-'
t_TIMES        = r'\*'
t_DIVIDE       = r'/'
t_EQUALS       = r'='
t_LPAREN       = r'\('
t_RPAREN       = r'\)'
t_NAME         = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_POW          = r'\^'
t_MOD          = r'\%'

####################################################################
#Funciones de análisis léxico
####################################################################

#VALORES TIPO FLOTANTES
def t_DOUBLE(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Double value too large %d", t.value)
        t.value = 0
    return t

#VALORES TIPO ENTERO
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
               ('left','TIMES','DIVIDE'),
               ('right','UMINUS'),
               ('right','POW','MOD'),
            )


####################################################################
#Funciones de análisis sintáctico
####################################################################
# dictionary of names
names = { }
def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    names[t[1]] = t[3]

        
    
def p_statement_expr(t):
    'statement : expression'
    print(t[1])
    
    
def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]
    
def p_expression_pow(t):
    'expression : expression POW expression'
    t[0] = pow(t[1],t[3])

def p_expression_mod(t):
    'expression : expression MOD expression'
    t[0] = t[1] % t[3]

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    '''expression : NUMBER
                  | DOUBLE'''

    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
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
