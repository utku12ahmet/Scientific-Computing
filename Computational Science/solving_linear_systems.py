import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = np.array([[2, -1, 3], 
              [1,  3, 2], 
              [4,  2, -1]])
B = np.array([5, 10, 3])  # Constant terms vector

solution = np.linalg.solve(A, B)

print("Solution:", solution)

x1, x2, x3 = solution

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

Z1 = (B[0] - A[0, 0] * X - A[0, 1] * Y) / A[0, 2]
Z2 = (B[1] - A[1, 0] * X - A[1, 1] * Y) / A[1, 2]
Z3 = (B[2] - A[2, 0] * X - A[2, 1] * Y) / A[2, 2]

ax.plot_surface(X, Y, Z1, alpha=0.5, rstride=100, cstride=100, color='r', label='Plane 1')
ax.plot_surface(X, Y, Z2, alpha=0.5, rstride=100, cstride=100, color='g', label='Plane 2')
ax.plot_surface(X, Y, Z3, alpha=0.5, rstride=100, cstride=100, color='b', label='Plane 3')

ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('X3')
ax.set_title('3D Solution of Linear System')

plt.show()
