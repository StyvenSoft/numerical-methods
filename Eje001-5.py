from tabulate import tabulate
import math

def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h

def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2*h)

def function(x):
    return math.cos(x)

x = 2.2

# Table for forward derivative
forward_table = []
for h in [0.5, 0.05, 0.01]:
    approx_derivative = forward_difference(function, x, h)
    percent_error = abs((-math.sin(x) - approx_derivative) / -math.sin(x)) * 100
    forward_table.append([h, approx_derivative, percent_error])

print("Table for forward derivative:\n")
print(tabulate(forward_table, headers=["h", "Approx Derivative", "Error %"], tablefmt="grid"))

# Table for backward derivative
backward_table = []
for h in [0.5, 0.05, 0.01]:
    approx_derivative = backward_difference(function, x, h)
    percent_error = abs((-math.sin(x) - approx_derivative) / -math.sin(x)) * 100
    backward_table.append([h, approx_derivative, percent_error])

print("\nTable for backward derivative:\n")
print(tabulate(backward_table, headers=["h", "Approx Derivative", "Error %"], tablefmt="grid"))

# Table for central derivative
central_table = []
for h in [0.5, 0.05, 0.01]:
    approx_derivative = central_difference(function, x, h)
    percent_error = abs((-math.sin(x) - approx_derivative) / -math.sin(x)) * 100
    central_table.append([h, approx_derivative, percent_error])

print("\nTable for central derivative:\n")
print(tabulate(central_table, headers = ["h", "Approx Derivative", "Error %"], tablefmt="grid"))
