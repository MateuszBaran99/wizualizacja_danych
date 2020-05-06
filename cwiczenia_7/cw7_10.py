import numpy as np

a = np.arange(81).reshape(9,9)
print(a, "\n")
print(a.reshape(81,1))
print(a.reshape(1,81))
print(a.reshape(27,3))