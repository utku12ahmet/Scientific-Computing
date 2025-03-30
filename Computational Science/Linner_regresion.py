import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


x = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75]).reshape(-1, 1)
y = np.array([220, 230, 250, 240, 260, 270, 280, 290, 310, 300])


model = LinearRegression()
model.fit(x, y)


m = model.coef_[0]  
b = model.intercept_  
print(f"y = {b:.2f} + {m:.2f}x")


y_pred = model.predict(x)


plt.scatter(x, y, color="blue", label="real data")  
plt.plot(x, y_pred, color="red", linewidth=2, label="Regresion line")  
plt.xlabel("X Değeri")
plt.ylabel("Y Değeri")
plt.title("Lineer regresion")
plt.legend()
plt.grid()
plt.show()
