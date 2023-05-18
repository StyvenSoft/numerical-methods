import math

# Definir la función a integrar
def f(x):
    return 1/(1+math.sin(x))

# Definir las funciones para los diferentes métodos

# Trapecio simple
def TrapecioSimple(a, b):
    return (b-a)*(f(a)+f(b))/2

def ErrorTrapecioSimple(a, b):
    return abs((IR-TrapecioSimple(a,b))/IR)*100

# Trapecio compuesto
def TrapecioCompuesto(a, b, n):
    h = (b-a)/n
    suma = 0
    for i in range(1,n):
        suma += f(a+i*h)
    return (h/2)*(f(a)+2*suma+f(b))

def ErrorTrapecioCompuesto(a, b, n):
    return abs((IR-TrapecioCompuesto(a,b,n))/IR)*100

# Simpson 1/3 simple
def Simpson13Simple(a, b):
    return (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6

def ErrorSimpson13Simple(a, b):
    return abs((IR-Simpson13Simple(a,b))/IR)*100

# Simpson 1/3 compuesto
def Simpson13Compuesto(a, b, n):
    h = (b-a)/n
    suma = 0
    for i in range(1,n):
        if i%2 == 0:
            suma += 2*f(a+i*h)
        else:
            suma += 4*f(a+i*h)
    return (h/3)*(f(a)+suma+f(b))

def ErrorSimpson13Compuesto(a, b, n):
    return abs((IR-Simpson13Compuesto(a,b,n))/IR)*100

# Simpson 3/8 simple
def Simpson38Simple(a, b):
    return (b-a)*(f(a)+3*f((2*a+b)/3)+3*f((a+2*b)/3)+f(b))/8

def ErrorSimpson38Simple(a, b):
    return abs((IR-Simpson38Simple(a,b))/IR)*100

# Simpson 3/8 compuesto
def Simpson38Compuesto(a, b, n):
    h = (b-a)/n
    suma = 0
    for i in range(1,n):
        if i%3 == 0:
            suma += 2*f(a+i*h)
        else:
            suma += 3*f(a+i*h)
    return (3*h/8)*(f(a)+suma+f(b))

def ErrorSimpson38Compuesto(a, b, n):
    return abs((IR-Simpson38Compuesto(a,b,n))/IR)*100

# Definir las entradas
a = 0
b = math.pi/2
IR = 0.694039

# Evaluar las reglas simples
# Trapecio simple
IT = TrapecioSimple(a, b)
ErrorT = ErrorTrapecioSimple(a, b)

print("Regla del trapecio simple")
print("Valor aproximado: ", IT)
print("Error porcentual: ", ErrorT)

# Simpson 1/3 simple
IS13 = Simpson13Simple(a, b)
ErrorS13 = ErrorSimpson13Simple(a, b)

print("\nRegla de Simpson 1/3 simple")
print("Valor aproximado: ", IS13)
print("Error porcentual: ", ErrorS13)

# Simpson 3/8 simple
IS38 = Simpson38Simple(a, b)
ErrorS38 = ErrorSimpson38Simple(a, b)

print("\nRegla de Simpson 3/8 simple")
print("Valor aproximado: ", IS38)
print("Error porcentual: ", ErrorS38)

# Evaluamos las reglas compuestas
n1 = 12
n2 = 15

# Trapecio compuesto
ITC1 = TrapecioCompuesto(a, b, n1)
ITC2 = TrapecioCompuesto(a, b, n2)
ErrorTC1 = ErrorTrapecioCompuesto(a, b, n1)
ErrorTC2 = ErrorTrapecioCompuesto(a, b, n2)

print("\nRegla del trapecio compuesto (n = 12)")
print("Valor aproximado: ", ITC1)
print("Error porcentual: ", ErrorTC1)

print("\nRegla del trapecio compuesto (n = 15)")
print("Valor aproximado: ", ITC2)
print("Error porcentual: ", ErrorTC2)

# Simpson 1/3 compuesto
IS131 = Simpson13Compuesto(a, b, n1)
IS132 = Simpson13Compuesto(a, b, n2)
ErrorS131 = ErrorSimpson13Compuesto(a, b, n1)
ErrorS132 = ErrorSimpson13Compuesto(a, b, n2)

print("\nRegla de Simpson 1/3 compuesta (n = 12)")
print("Valor aproximado: ", IS131)
print("Error porcentual: ", ErrorS131)

print("\nRegla de Simpson 1/3 compuesta (n = 15)")
print("Valor aproximado: ", IS132)
print("Error porcentual: ", ErrorS132)

# Simpson 3/8 compuesto
IS381 = Simpson38Compuesto(a, b, n1)
IS382 = Simpson38Compuesto(a, b, n2)
ErrorS381 = ErrorSimpson38Compuesto(a, b, n1)
ErrorS382 = ErrorSimpson38Compuesto(a, b, n2)

print("\nRegla de Simpson 3/8 compuesta (n = 12)")
print("Valor aproximado: ", IS381)
print("Error porcentual: ", ErrorS381)

print("\nRegla de Simpson 3/8 compuesta (n = 15)")
print("Valor aproximado: ", IS382)
print("Error porcentual: ", ErrorS382)