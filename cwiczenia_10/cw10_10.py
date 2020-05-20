import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 21, 1)
print(x)
plt.subplot(1,2,1)
plt.plot(1/x, label = "f(x) = 1/x")
plt.axis([0, 20, 0, 1])
plt.xlabel("x")
plt.ylabel("f(x)")
plt.annotate('x = 5, y = 0.170966',
            xy=(5, 0.170966), xycoords='data',
            xytext=(100, 30), textcoords='offset points',
            arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
plt.legend()

plt.subplot(1,2,2)
y = np.arange(0, 30, 0.1)
s = np.sin(y)
c = np.cos(y)
plt.plot(y, s, label='sin(x)')
plt.plot(y, c, label='cos(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.annotate('x = 6.27 , y = 1',
            xy=(6.27, 1), xycoords='data',
            xytext=(100, 30), textcoords='offset points',
            arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')

plt.title("Wykres sin(x) oraz cos(x)")

plt.legend()
plt.show()