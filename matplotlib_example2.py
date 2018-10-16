import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
sinx = np.sin(x)
cosx = np.cos(x)

# plt.plot(x, sinx, '-b', x, sinx, 'ob', x, cosx, '-r', x, cosx, 'or')
# plt.xlabel('X label')
# plt.ylabel('Y label')
# plt.legend()
# plt.show()

plt.plot(x, sinx, label = 'sinx', color = 'b', linestyle = '--', linewidth = 2)
plt.plot(x, cosx, label = 'cosx', color = 'r', linestyle = '-', linewidth = 2)
plt.xlabel('X label')
plt.ylabel('Y label')
plt.legend()
plt.show()
