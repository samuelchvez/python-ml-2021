import numpy as np


sigmoid = lambda z: 1.0 / (1 + np.exp(-z))


def perceptron(X, W):
    return sigmoid(X @ W.T)


print(perceptron(
    np.array([-1, 2, 0]).reshape(1, 3),
    np.array([9, 8, 7]).reshape(1, 3),
))