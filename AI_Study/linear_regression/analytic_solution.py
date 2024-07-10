# 代码实战解析模型

import numpy as np

import matplotlib.pyplot as plt

np.random.seed(42)
X = 2*np.random.rand(100, 1)
print(len(X))
print(X)

y = 5 + 4*X + np.random.randn(100, 1)

X_b = np.c_[np.ones((100, 1)), X]

theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

print(theta)

X_new = np.array([[0],
                  [2]])

X_new_b = np.c_[np.ones((2, 1)), X_new]

print(X_new_b)

y_predict = X_new_b.dot(theta)

print(y_predict)

plt.plot(X_new, y_predict, 'r-')
plt.plot(X, y, 'b.')
plt.axis([0, 2, 0, 15])
plt.show()
