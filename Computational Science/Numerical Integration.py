import numpy as np
import matplotlib.pyplot as plt

def rectangle_method(f, a, b, n):
    dx = (b - a) / n
    total_area = 0
    for i in range(n):
        total_area += f(a + i * dx) * dx
    return total_area

def trapezoid_method(f, a, b, n):
    dx = (b - a) / n
    total_area = (f(a) + f(b)) / 2
    for i in range(1, n):
        total_area += f(a + i * dx)
    return total_area * dx

def func(x):
    return x**2

a = 0
b = 10
n = 1000

rectangle_area = rectangle_method(func, a, b, n)
trapezoid_area = trapezoid_method(func, a, b, n)

x = np.linspace(a, b, 100)
y = func(x)

plt.plot(x, y, label='Function', color='green')
plt.fill_between(x, y, color='lightgreen', alpha=0.5)
plt.title(f'Rectangle Method Area: {rectangle_area:.4f}, Trapezoid Method Area: {trapezoid_area:.4f}')
plt.legend()
plt.show()
