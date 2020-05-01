import numpy as np

def funkcja(x, y):
    return np.logspace(1, y, base=x, num=y, dtype="int")

print(funkcja(2, 4))