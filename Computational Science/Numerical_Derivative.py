import numpy as np
import matplotlib.pyplot as plt

def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def func(x):
    return x**2

x = np.linspace(-10, 10, 100)
y = func(x)

h = 0.1
forward_derivative = forward_difference(func, x, h)
central_derivative = central_difference(func, x, h)

plt.plot(x, y, label='Function', color='green')
plt.plot(x, forward_derivative, label='Forward Difference Derivative', color='blue')
plt.plot(x, central_derivative, label='Central Difference Derivative', color='red')
plt.legend()
plt.show()
