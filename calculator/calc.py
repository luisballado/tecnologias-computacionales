
import math

#####################################################################
#MODULARIDAD ALTA COHESION DEBIL ACOPLAMIENTO
#HERRAMIENTA
#AUTOMATICO
#SERIALIZACION DE OBJETOS guardar el estado de un objeto en disco
#Objeto vive en tiempo de ejecucion
#Clase vive en tiempo de asignacion
#####################################################################
# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------
####################################################################
# Lista de tokens
####################################################################
tokens = (
    'NAME',
    'NUMBER',
    'DOUBLE',
    'FUNCTION',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'LPAREN','RPAREN',
    'POW',
    'MOD',
    'SET',
    'INTERSECTION',
    'UNION',
    'DSIM',
    'DIFF',
    'VACIO',
    'COMP'
    )

####################################################################
# Especificación de los tokens
####################################################################
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
t_UNION        = r'U'
t_INTERSECTION = r'∩'
t_DSIM         = r'ß' #r'^[g]$' #solo uno
t_DIFF         = r'\\'
t_COMP         = r'\''
t_VACIO        = r'ø'

####################################################################
# Funciones de análisis léxico
####################################################################
# FUNCIONES TODAS
def t_FUNCTION(t):
    r'invsen|invcos|invtan|sen|cos|tan|log10|log2|sqrt|SQRT|nlog|ln|tanh|cosh|senh|asinh|acosh|atanh'
    return t

####################################################################
# FUNCIONES VALORES TIPO DOUBLE
####################################################################
def t_DOUBLE(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Double value too large %d", t.value)
        t.value = 0
    return t

####################################################################
#VALORES TIPO ENTERO
####################################################################
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
# Contruccion del lexer
import ply.lex as lex
lexer = lex.lex()

####################################################################
# Reglas de Parsing
####################################################################
precedence = ( ('left','PLUS','MINUS'),
               ('left','TIMES','DIVIDE','DSIM'),
               ('right','UMINUS','FUNCTION'),
               ('right','POW','MOD'),
            )


####################################################################
#Funciones de análisis sintáctico
####################################################################

names = { }

# Las asignaciones es un diccionatio
def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    print('ASIGNACION')
    #EJEMPLO
    #A=0
    #t[1] -> A
    #t[2] -> =
    #t[3] -> 0
    print(t[1])
    if t[1] in names:
        print('Ya existe algo y es')
        print(names[t[1]])
        #qutar los elemento del viejo conjunto a UNI pero que no formen parte de los otros conjuntos

        quitar = names[t[1]].difference(t[3])
        
        for _r_ in quitar:
            #iter some way
            print(names.keys())
            for _n_ in names.keys():
                print(_n_)
                if _r_ in names[_n_]:
                    print('Saltar')
                    print('Que Salto?')
                    print(_r_)
                else:
                    names['UNI'].remove(_r_)
                                            
    #print(t[2])
    #print(t[3])
    names[t[1]] = t[3]

####################################################################
# IMPRIME RESPUESTA DE UNA ASIGNACION
####################################################################
def p_statement_expr(t):
    'statement : expression'
    print(t[1])

####################################################################
# Expresiones con dos operadores de la forma 1 + 1
####################################################################
def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    
    if   t[2] == '+': t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

####################################################################
# Funcion que regresa el valor de x elevado a la y
####################################################################
def p_expression_pow(t):
    'expression : expression POW expression'
    t[0] = pow(t[1],t[3])

####################################################################
# Funcion que regresa el modulo entre dos valores
####################################################################
def p_expression_mod(t):
    'expression : expression MOD expression'
    t[0] = t[1] % t[3]

####################################################################
# Funcion que engloba todas las funciones
####################################################################
def p_function(t):
    'expression : FUNCTION LPAREN expression RPAREN'

    #SENO
    if t[1] == 'sen':
        t[0] = math.sin(t[3])
    #COSENO
    elif t[1] == 'cos':
        t[0] = math.cos(t[3])
    #TANGENTE
    elif t[1] == 'tan':
        t[0] = math.tan(t[3])
    #TANGENTE INVERSA
    elif t[1] == 'invtan':
        t[0] = math.atan(t[3])
    #SENO INVERSO
    elif t[1] == 'invsen':
        t[0] = math.asin(t[3])
    #COSENO INVERSO
    elif t[1] == 'invcos':
        t[0] = math.acos(t[3])
    #TANGENTE HIPERBOLICO
    elif t[1] == 'tanh':
        t[0] = math.tanh(t[3])
    #COSENO HIPERBOLICO
    elif t[1] == 'cosh':
        t[0] = math.cosh(t[3])
    #SENO HIPERBOLICO
    elif t[1] == 'senh':
        t[0] = math.senh(t[3])
    #SENO HIPERBOLICO INVERSO
    elif t[1] == 'asinh':
        t[0] = math.asinh(t[3])
    #COSENO HIPERBOLICO INVERSO    
    elif t[1] == 'acosh':
        t[0] = math.acosh(t[3])
    #TANGENTE HIPERBOLICO INVERSO
    elif t[1] == 'atanh':
        t[0] = math.atanh(t[3])
    #LOGARITMO BASE 10
    elif t[1] == 'log10':
        t[0] = math.log(t[3],10)
    #LOGARITMO BASE 2
    elif t[1] == 'log2':
        t[0] = math.log(t[3],2)
    #RAIZ CUADRADA
    elif t[1] == 'sqrt':
        t[0] = math.sqrt(t[3])
    #LOGARITMO NATURAL
    elif ((t[1] == 'ln') or (t[1] == 'nlog')):
        t[0] = math.log(t[3])
    else:
        print('FUNCION NO IMPLEMENTADA')

####################################################################
# EXPRESAR NUMEROS NEGATIVOS
####################################################################
def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

####################################################################
# CREACION DE GRUPOS
####################################################################
def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

####################################################################
# FUNCION PARA OPERACIONES CON CONJUNTOS
####################################################################
def p_expression_set(t):
    'expression : SET'
    #print('SET')
    #t[0] = t[1]
    #print('#t1')
    #print(t[1])
    
    t[0] = set() #Existe algo en el set
    
    #verificar aqui si existe el UNIVERSAL
    if 'UNI' not in names:
        #print('NO HAY UNIVERSAL') crear el UNIVERSAL
        names['UNI'] = set()
        U = names['UNI']
    else:
        U = names['UNI']

        #Si el set muto identificar para replicarlo en UNI
        
        '''
        if t[1] in names:
            for s in t[3]:
                names['UNI'].remove(s)
        '''

    #Agregar los elementos al UNIVERSAL
    for s in t[1]:
        t[0].add(s)
        U.add(s)
        
    #No commas en sets de cardinalidad uno
    if ',' in t[0]:
        t[0].remove(',')
        U.remove(',')

    t[0].remove('{')
    t[0].remove('}')
    U.remove('{')
    U.remove('}')
    
####################################################################
# UNION DE CONJUNTOS
####################################################################
def p_expression_union(t):
    'expression : expression UNION expression'
    t[0] = t[1].union(t[3])
    '''
    for i in range(len(t)):
        print(t[i])
    '''

####################################################################
# INTERSECCION DE CONJUNTOS
####################################################################
def p_expression_intersection(t):
    'expression : expression INTERSECTION expression'
    t[0] = t[1].intersection(t[3])

####################################################################
# DIFERENCIA SIMETRICA DE CONJUNTOS (QUITA LO QUE CONTENGA EN DOS)
####################################################################
def p_expression_dsim(t):
    'expression : expression DSIM expression'
    print('DSIM')
    t[0] = t[1].symmetric_difference(t[3])

####################################################################
# DIFERENCIA ENTRE DOS CONJUNTOS
####################################################################
def p_expression_diff(t):
    'expression : expression DIFF expression'
    t[0] = t[1].difference(t[3])

####################################################################
# COMPLEMENTO DADO UN CONJUNTO (UNIVERSE - SET)
####################################################################
def p_expression_comp(t):
    'expression : expression COMP'
    t[0] = names['UNI'] - t[1]

####################################################################
# CONJUNTO VACIO
####################################################################
def p_expression_vacio(t):
    'expression : VACIO'
    t[0] = set()

####################################################################
# NUMERO O DOBLE
####################################################################
def p_expression_number(t):
    '''expression : NUMBER
                  | DOUBLE'''
    t[0] = t[1]

####################################################################
#IMPRIMIR LO QUE TENGA EN MEMORIA
####################################################################
def p_expression_name(t):
    'expression : NAME'
    
    try:
        #print('El t0 es')
        #t es un objeto
        
        t[0] = names[t[1]]
                
        print('Es todo el dict')
        print(names)
        #print('t[1]')
        #print(type(t[1]))
        #print(t[0])
        #print(type(names[t[1]]))
                
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
