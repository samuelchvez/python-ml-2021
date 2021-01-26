import numpy as np

print(type(np.arange(10, 20, 2)))

a = np.arange(1, 10).reshape((3, 3))
b = np.arange(10, 13).reshape((3, 1))

print(a)
print(b)
print(a.shape)
print(b.shape)

print(b.T @ a)