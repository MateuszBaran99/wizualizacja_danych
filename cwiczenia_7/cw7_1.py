import numpy as np

a = np.arange(0,3,1).reshape(1, 3)
print(a, "\n")
b = np.arange(5,8,1).reshape(1, 3)
print(b, "\n")
c = a*b
print(c)