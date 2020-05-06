import numpy as np

a = np.arange(5,11,1).reshape(2, 3)
a = np.sin(a)
print(a, "\n")
b = np.arange(5,11,1).reshape(2, 3)
b = np.cos(a)
print(b, "\n")
print(np.add(a, b))
