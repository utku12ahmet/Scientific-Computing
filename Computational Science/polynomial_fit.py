import numpy as np
import matplotlib.pyplot as plt

def polynomial_fit(x, y, degree):
    coefficients = np.polyfit(x, y, degree)
    polynomial = np.poly1d(coefficients)
    return polynomial

x = np.linspace(-10, 10, 100)
y = x**3 - 5*x**2 + 2*x + 7 + np.random.normal(0, 10, len(x))

polynomial = polynomial_fit(x, y, 3)

x_fit = np.linspace(-10, 10, 200)
y_fit = polynomial(x_fit)

plt.scatter(x, y, label='Data', color='red')
plt.plot(x_fit, y_fit, label='Polynomial Fit', color='blue')
plt.legend()
plt.show()
