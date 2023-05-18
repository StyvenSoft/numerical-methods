import numpy as np
import matplotlib.pyplot as plt

# Define the ODE and initial condition
def f(x, y):
    return 1.8*x + 2.1*y - 1.2
y0 = 1.0

# Define the step sizes
h_values = [0.5, 0.1, 0.05]

# Define the range of x values to solve for
x_values = np.arange(1.0, 3.21, 0.01)

# Solve the ODE using the Euler, second-order Runge-Kutta, and fourth-order Runge-Kutta methods
for h in h_values:
    x = [1.0]
    y = [y0]
    for i in range(len(x_values)-1):
        y_next = y[-1] + h*f(x[-1], y[-1])
        x_next = x[-1] + h
        x.append(x_next)
        y.append(y_next)
        
    plt.plot(x, y, label=f"h = {h}")
    
# Add legend and axis labels
plt.legend()
plt.xlabel("x")
plt.ylabel("y")

# Show the plot
plt.show()
