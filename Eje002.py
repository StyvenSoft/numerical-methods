import math
from tabulate import tabulate # se utiliza para presentar los datos en forma de tabla

# Definir la función
def f(x):
    return math.cos(x)

# Esquema de la segunda derivada de forward
def segunda_derivada_forward(f, x, h):
    return (f(x + 2*h) - 2*f(x + h) + f(x))/h**2

# Esquema de la segunda derivada de backward
def segunda_derivada_backward(f, x, h):
    return (f(x) - 2*f(x - h) + f(x - 2*h))/h**2

# Esquema de la segunda derivada central
def segunda_derivada_central(f, x, h):
    return (f(x + h) - 2*f(x) + f(x - h))/h**2

# Ingreso de datos
x = 2.2
h_values = [0.5, 0.05, 0.01]

# Calculo de las derivadas para cada valor de h
resultados = []
for h in h_values:
    # Calculo de la segunda derivada utilizando los tres esquemas
    fpp_forward = segunda_derivada_forward(f, x, h)
    fpp_backward = segunda_derivada_backward(f, x, h)
    fpp_central = segunda_derivada_central(f, x, h)
    
    # Calcular el error relativo para cada esquema
    fpp_real = -math.cos(x)
    error_forward = abs((fpp_forward - fpp_real)/fpp_real)*100
    error_backward = abs((fpp_backward - fpp_real)/fpp_real)*100
    error_central = abs((fpp_central - fpp_real)/fpp_real)*100
    
    # Guardar los resultados en una lista
    resultados.append([h, fpp_forward, error_forward, fpp_backward, error_backward, fpp_central, error_central])

# Tabla comparativa con los resultados obtenidos y la respuesta analítica
header = ["Tamaño h", "f''(x) Forward", "Error Forward (%)", "f''(x) Backward", "Error Backward (%)", "f''(x) Central", "Error Central (%)"]
tabla = tabulate(resultados, headers=header)

print(tabla)