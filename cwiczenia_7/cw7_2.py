import numpy as np

a = np.arange(1,10,1).reshape(3, 3)
print(a, "\n")
b = np.arange(5,14,1).reshape(3, 3)
print(b, "\n")

#kolumny
print(a.min(axis=0))
print(b.min(axis=0), "\n")
#wiersze
print(a.min(axis=1))
print(b.min(axis=1))