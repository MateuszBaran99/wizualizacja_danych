import numpy as np

a = np.arange(1,10,1).reshape(3, 3)
for b in a.flat:
    print(b)