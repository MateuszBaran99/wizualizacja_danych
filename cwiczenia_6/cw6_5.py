import numpy as np

def funkcja(x):
    return np.diag(np.arange(x, 0, step=-1))

print(funkcja(5))