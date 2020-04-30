import numpy as np


def macierz(n):
    a = np.array([np.arange(1, n*n+1)])
    b = a.reshape(n, n)
    return b

print(macierz(5))