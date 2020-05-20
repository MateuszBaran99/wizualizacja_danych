import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 21, 1)
print(x)
plt.plot(1/x, label = "f(x) = 1/x")
plt.axis([0, 20, 0, 1])
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()