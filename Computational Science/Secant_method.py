import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2 - 2


def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    iter_count = 0
    x_values = [x0, x1]
    while iter_count < max_iter:

        x2 = x1 - f(x1) * (x0 - x1) / (f(x0) - f(x1))
        x_values.append(x2)
        

        if abs(x2 - x1) < tol:
            break
        
        
        x0, x1 = x1, x2
        iter_count += 1
    
    return x2, iter_count, x_values


x0 = 1.0
x1 = 2.0

root, iterations, x_values = secant_method(f, x0, x1)


print(f"Root: {root}")
print(f"iteration count: {iterations}")


x = np.linspace(-2, 2, 400)
y = f(x)

plt.plot(x, y, label=r'$f(x) = x^2 - 2$')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)


for i in range(1, len(x_values)):
    plt.plot([x_values[i-1], x_values[i]], [f(x_values[i-1]), f(x_values[i])], 'ro-', label="Secant step" if i == 1 else "")
    
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Secant method and function graph')
plt.grid(True)
plt.show()
