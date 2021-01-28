import numpy as np

# print(type(np.arange(10, 20, 2)))

# a = np.arange(1, 10).reshape((3, 3))
# b = np.arange(10, 13).reshape((3, 1))

# print(a)
# print(b)
# print(a.shape)
# print(b.shape)

# print(b.T @ a)

# 5 + 6 * 1 + 7 * 2
# 5 + 6 * 3 + 7 * 4

X = np.array([
    [1, 3],
    [2, 4],
])

X = np.vstack((
    np.ones(2).reshape(1, 2),
    X
))

Theta = np.array([
    [5],
    [6],
    [7],
])

print(X.T @ Theta)

