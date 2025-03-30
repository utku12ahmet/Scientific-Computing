import matplotlib.pyplot as plt

# Function g(x) for fixed-point iteration
def g(x):
    return (1 - x) ** (1/3)

# Fixed-Point Iteration function
def fixed_point_iteration(x0, tol=1e-6, max_iter=100):
    x_values = [x0]
    for i in range(max_iter):
        x_new = g(x0)
        x_values.append(x_new)
        
        # Convergence check
        if abs(x_new - x0) < tol:
            break
        x0 = x_new

    return x_new, x_values

# Initial guess
x0 = 0.5
root, iter_values = fixed_point_iteration(x0)

# Print the result
print("Root approximation:", root)

# Plot the iterations
plt.plot(iter_values, marker='o', linestyle='-', color='b', label='Iterations')
plt.axhline(root, color='r', linestyle='--', label='Final Root')
plt.xlabel("Iteration Step")
plt.ylabel("x Value")
plt.title("Fixed-Point Iteration Process")
plt.legend()
plt.show()
