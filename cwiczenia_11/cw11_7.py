import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random

fig = plt.figure()
ax = fig.gca( projection = '3d' )

color = ["r", "b", "m", "c", "g"]
marker = ["p", "h", "X", "D", "*"]

n = 4
x = np.random.rand(n)
y = np.random.rand(n)
z = np.random.rand(n)
ax.scatter(x, y, z, c=color[random.randint(0, 4)], marker=marker[random.randint(0, 4)])


m = 10
x = np.random.rand(m)
y = np.random.rand(m)
z = np.random.rand(m)
ax.plot(x, y, z, c=color[random.randint(0, 4)])

plt.show()
