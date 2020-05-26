import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random


ax = plt.subplot(111, projection="3d")

color = ["r", "b", "m", "c", "g"]
marker = ["p", "h", "X", "D", "*"]

n = 20
for i in range(5):
    x = np.random.rand(n)
    y = np.random.rand(n)
    z = np.random.rand(n)
    ax.scatter(x, y, z, c=color[random.randint(0, 4)], marker=marker[random.randint(0, 4)])

ax.set_xlabel( 'X' )
ax.set_ylabel( 'Y' )
ax.set_zlabel( 'Z' )
plt.show()


