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
    'FUNCTION','PLUS','MINUS',
    'TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN','POW','MOD',
    'SET','INTERSECTION','UNION',
    'DSIM','DIFF','VACIO','UNIVERSE'
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
t_SET          = r'\{([^]]*)\}'
t_UNION        = r'∪'
t_INTERSECTION = r'∩'
t_DSIM         = r'ß'
t_DIFF         = r'\\'
#t_COMP         = r'[A-Z]\''
t_VACIO        = r'ø'
t_UNIVERSE     = r'µ'

####################################################################
#Funciones de análisis léxico
####################################################################
#FUNCIONES TODAS
def t_FUNCTION(t):
    r'invsen|invcos|invtan|sen|cos|tan|log10|log2|sqrt|SQRT|nlog|ln|tanh|cosh|senh|asinh|acosh|atanh'
    return t

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
               ('right','UMINUS','FUNCTION'),
               ('right','POW','MOD'),
            )


####################################################################
#Funciones de análisis sintáctico
####################################################################
# dictionary of names
names = { }
def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    #print('ASSIGN')
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    #print("statement_expr")
    print(t[1])
    
def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    #print('EXPRESSION')
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

def p_function(t):
    'expression : FUNCTION LPAREN expression RPAREN'
    #print('FUNCION')
    
    if t[1] == 'sen':
        t[0] = math.sin(t[3])
        #print('SEN')
    elif t[1] == 'cos':
        t[0] = math.cos(t[3])
        #print('COS')
    elif t[1] == 'tan':
        t[0] = math.tan(t[3])
        #print('TAN')
    elif t[1] == 'invtan':
        t[0] = math.atan(t[3])
        #print('INV TAN')
    elif t[1] == 'invsen':
        t[0] = math.asin(t[3])
        #print('INV SEN')
    elif t[1] == 'invcos':
        t[0] = math.acos(t[3])
        #print('INV COS')
    elif t[1] == 'tanh':
        t[0] = math.tanh(t[3])
    elif t[1] == 'cosh':
        t[0] = math.cosh(t[3])
    elif t[1] == 'senh':
        t[0] = math.senh(t[3])
    elif t[1] == 'asinh':
        t[0] = math.asinh(t[3])
    elif t[1] == 'acosh':
        t[0] = math.acosh(t[3])
    elif t[1] == 'atanh':
        t[0] = math.atanh(t[3])
    elif t[1] == 'log10':
        t[0] = math.log(t[3],10)
        #print('LOG10')
    elif t[1] == 'log2':
        t[0] = math.log(t[3],2)
        #print('LOG2')
    elif t[1] == 'sqrt':
        t[0] = math.sqrt(t[3])
        #print('SQRT')
    elif ((t[1] == 'ln') or (t[1] == 'nlog')):
        t[0] = math.log(t[3])
        #print('LOG NAT')
    else:
        print('ALGO MAS')
        
def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    #print('GROUP')
    t[0] = t[2]

def p_expression_set(t):
    'expression : SET'
    t[0] = t[1]
    t[0] = set()
    
    for s in t[1]:
        t[0].add(s)

    #No commas en sets de cardinalidad uno
    if len(t[1])>3:
        t[0].remove(',')

    t[0].remove('{')
    t[0].remove('}')

def p_expression_union(t):
    'expression : expression UNION expression'
    t[0] = t[1].union(t[3])

def p_expression_intersection(t):
    'expression : expression INTERSECTION expression'
    t[0] = t[1].intersection(t[3])

def p_expression_dsim(t):
    'expression : expression DSIM expression'
    t[0] = t[1].symmetric_difference(t[3])

def p_expression_diff(t):
    'expression : expression DIFF expression'
    t[0] = t[1].difference(t[3])

'''
def p_expression_comp(t):
    'expression : expression COMP'
    #Universe - set
    print('HOLA')
'''
def p_expression_vacio(t):
    'expression : VACIO'
    #COMP t_VACIO t_UNIVERSE
    print('HOLA')
    t[0] = set()
    
'''
def p_expression_universe(t):
    #COMP t_VACIO t_UNIVERSE
    t[0] = set()
'''
def p_expression_number(t):
    '''expression : NUMBER
                  | DOUBLE'''
    #print('NUMBER')
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
