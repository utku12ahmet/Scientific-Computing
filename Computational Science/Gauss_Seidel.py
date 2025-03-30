import numpy as np
import matplotlib.pyplot as plt

def gauss_seidel(A, B, tol=1e-6, max_iter=100):
    n = len(B)
    X = np.zeros(n)
    iterations = [X.copy()]
    
    for _ in range(max_iter):
        X_new = X.copy()
        for i in range(n):
            sum1 = sum(A[i, j] * X_new[j] for j in range(i))
            sum2 = sum(A[i, j] * X[j] for j in range(i + 1, n))
            X_new[i] = (B[i] - sum1 - sum2) / A[i, i]
        
        iterations.append(X_new.copy())
        
        if np.linalg.norm(X_new - X, ord=np.inf) < tol:
            break
        X = X_new
    
    return X, iterations

A = np.array([[4, -1, 0], 
              [-1, 4, -1], 
              [0, -1, 4]])

B = np.array([15, 10, 10])

solution, iter_steps = gauss_seidel(A, B)

print("Solution:", solution)

fig, ax = plt.subplots()
ax.set_title("Convergence of Gauss-Seidel Method")
ax.set_xlabel("Iteration Step")
ax.set_ylabel("Value of Variables")

for i in range(len(solution)):
    ax.plot(range(len(iter_steps)), [step[i] for step in iter_steps], marker='o', label=f"x{i+1}")

ax.legend()
ax.grid()
plt.show()
