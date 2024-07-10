import numpy as np

X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 6, 8, 10])

w = 0.0
b = 0.0

learning_rate = 0.01
epochs = 1000

for i in range(epochs):
    y_predicted = w * X + b
    loss = np.mean((y_predicted - Y)**2)
    dw = -2 * np.mean(X * (Y - y_predicted))
    db = -2 * np.mean(Y - y_predicted)
    w -= learning_rate * dw
    b -= learning_rate * db
    if i % 100 == 0:
        print(f"Epoch: {i}: w = {w}, b = {b}, loss = {loss}")

print(f"Final y = {w}x + {b}")
