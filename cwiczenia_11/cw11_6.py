import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random

ax1 = plt.subplot(121, projection="3d")

color = ["r", "b", "m", "c", "g"]
marker = ["p", "h", "X", "D", "*"]

n = 20
x = np.random.rand(n)
y = np.random.rand(n)
z = np.random.rand(n)
ax1.scatter(x, y, z, c=color[random.randint(0, 4)], marker=marker[random.randint(0, 4)])

ax2 = plt.subplot(122, projection="3d")
m = 5
x = np.random.rand(m)
y = np.random.rand(m)
z = np.random.rand(m)
ax2.plot(x, y, z, c=color[random.randint(0, 4)], marker=marker[random.randint(0, 4)])

plt.show()
