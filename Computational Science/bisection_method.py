import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - x - 2  # Example function

def bisection_method_plot(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Invalid interval: f(a) and f(b) must have opposite signs.")
        return None

    x_values = np.linspace(a - 1, b + 1, 400)  # X-axis range for plotting
    y_values = f(x_values)  

    plt.figure(figsize=(8, 6))  
    plt.plot(x_values, y_values, label="f(x)", color="blue")  # Function plot
    plt.axhline(0, color="black", linewidth=1)  # X-axis

    iteration = 0
    midpoints = []

    while (b - a) / 2 > tol and iteration < max_iter:
        xr = (a + b) / 2  # Midpoint
        midpoints.append(xr)

        plt.scatter(xr, f(xr), color="red", marker="*", s=100)  # Mark midpoint
        
        if f(xr) == 0:
            break  # Exact root found
        elif f(a) * f(xr) < 0:
            b = xr
        else:
            a = xr
        iteration += 1

    plt.title("Bisection Method Iterations")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()

    return xr

# Example usage
guess1=int(input("first guess"))
guess2=int(input("second guess"))
root = bisection_method_plot(guess1,guess2)
print(f"Approximate root: {root}") 