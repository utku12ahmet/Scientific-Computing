import numpy as np
import matplotlib.pyplot as plt

# Function f(x) and its derivative f'(x)
def f(x):
    return x**3 - x - 2

def df(x):  # Derivative of f(x)
    return 3*x**2 - 1

# Newton-Raphson Method
def newton_raphson(x0, tol=1e-6, max_iter=100):
    x_values = [x0]  # Store iteration steps for visualization
    for i in range(max_iter):
        x_new = x0 - f(x0) / df(x0)  # Newton-Raphson formula
        x_values.append(x_new)
        
        # Convergence check
        if abs(x_new - x0) < tol:
            break
        x0 = x_new

    return x_new, x_values

# Initial guess
x0 = 1.5
root, iter_values = newton_raphson(x0)

# Print result
print("Root approximation:", root)

# Visualization
x = np.linspace(-2, 3, 1000)  # X-axis range
y = f(x)  # Compute function values

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$f(x) = x^3 - x - 2$', color='blue')
plt.axhline(0, color='black', linestyle='--')  # X-axis (y=0)
plt.scatter(iter_values, [f(i) for i in iter_values], color='red', label="Iterations")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Newton-Raphson Iteration")
plt.legend()
plt.grid()
plt.show()
