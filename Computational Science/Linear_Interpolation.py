import numpy as np
import matplotlib.pyplot as plt

# Function to find the root
def f(x):
    return x**3 - x - 2

# False Position Method
def false_position(lower_bound, upper_bound, tol=1e-4, max_iter=20):
    if f(lower_bound) * f(upper_bound) >= 0:
        print("Invalid interval! The root may not exist in this range.")
        return None
    
    iteration = 0
    prev_root = lower_bound  # Previous root value
    error = 100  # Initial large error
    root_list = []  # List to store root values

    # Set up the plot
    plt.figure(figsize=(8, 5))

    while error > tol and iteration < max_iter:
        # False Position formula
        root = upper_bound - (f(upper_bound) * (lower_bound - upper_bound)) / (f(lower_bound) - f(upper_bound))
        root_list.append(root)

        # Calculate relative error
        if iteration > 0:
            error = abs((root - prev_root) / root) * 100
        prev_root = root

        # Determine the new search interval
        if f(lower_bound) * f(root) < 0:
            upper_bound = root  # Root is in the left subinterval
        else:
            lower_bound = root  # Root is in the right subinterval

        iteration += 1

        # Plot function and current root
        x_vals = np.linspace(lower_bound - 1, upper_bound + 1, 100)
        y_vals = f(x_vals)
        
        plt.plot(x_vals, y_vals, label=f"Iteration {iteration}")
        plt.axhline(0, color="black", linewidth=0.8)  # X-axis
        plt.scatter(root, f(root), color="red", marker="o", label=f"Root {iteration}")

    # Show the final plot
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("False Position Method - Iterative Root Finding")
    plt.grid()
    plt.show()

    return root_list

# Example usage
roots = false_position(1, 2)
print("Estimated Roots:", roots)
