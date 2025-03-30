import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.array([
        x**2 + y**2 - 4,  # Örnek denklem 1
        x - y             # Örnek denklem 2
    ])

def partial_derivatives(x, y):
    return np.array([
        [2*x, 2*y],  # f1'in türevleri
        [1, -1]      # f2'nin türevleri
    ])

def newton_raphson_custom(x0, y0, tol=1e-6, max_iter=20):
    x_vals, y_vals = [x0], [y0]
    for _ in range(max_iter):
        J = partial_derivatives(x0, y0)
        F = f(x0, y0)
        
        # Verilen yönteme göre güncelleme formülü
        xi_plus1 = -F[0] + x0 * J[0, 0] + y0 * J[0, 1]
        yi_plus1 = -F[1] + x0 * J[1, 0] + y0 * J[1, 1]
        
        x0, y0 = xi_plus1, yi_plus1
        x_vals.append(x0)
        y_vals.append(y0)
        
        if np.linalg.norm(F) < tol:
            break
    return x0, y0, x_vals, y_vals

# Başlangıç tahmini
x0, y0 = 2.0, 1.5
root_x, root_y, x_vals, y_vals = newton_raphson_custom(x0, y0)

# Grafik çizimi
x_range = np.linspace(-3, 3, 100)
y_range = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x_range, y_range)
F1 = X**2 + Y**2 - 4
F2 = X - Y

plt.figure(figsize=(8, 6))
plt.contour(X, Y, F1, levels=[0], colors='b')
plt.contour(X, Y, F2, levels=[0], colors='r')
plt.plot(x_vals, y_vals, 'ko-', label="Iterations")
plt.scatter(root_x, root_y, color='g', s=100, label="Root")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Newton-Raphson Method")
plt.grid()
plt.show()

print(f"Approximate root: x = {root_x}, y = {root_y}")