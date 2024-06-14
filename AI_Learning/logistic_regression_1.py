import numpy as np


def sigmoid(z):
    return 1/(1+np.exp(-z))


def compute_loss(y, y_hat):
    return -np.mean(y*np.log(y_hat)+(1 - y) * np.log(1 - y_hat))


X = np.array([[0.5], [2.3], [2.9]])
Y = np.array([0, 1, 1])

w = np.random.rand(X.shape[1], 1)
b = np.random.rand()

learning_rate = 0.01
epochs = 1000

for i in range(epochs):
    z = np.dot(X, w) + b
    y_hat = sigmoid(z)
    y_hat = y_hat.squeeze()
    loss = compute_loss(Y, y_hat)
    dz = y_hat - Y
    dw = np.dot(X.T, dz) / len(Y)

    db = np.sum(dz) / len(Y)

    w -= learning_rate * dw
    b -= learning_rate * db

    if i % 100 == 0:
        print(f"Epoch:{i}: loss={loss}")


print("Training complete")

