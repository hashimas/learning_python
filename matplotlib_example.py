import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 50)
sinx = np.sin(x)
# plt.plot(x, sinx, 'o')
# plt.show()

cosx = np.cos(x)
# plt.plot(x, sinx, '-b', x, sinx, 'ob', x, cosx, '-r', x, cosx, 'or')
# plt.xlabel('this is x')
# plt.ylabel('this is y')
# plt.title('my first plot')
# plt.show()

#step by step
plt.plot(x, sinx, label='Sin(x)', color ='blue', linestyle='-',linewidth = 2)
plt.plot(x, cosx, label ='Cos(x)', color = 'red', linestyle = '--', linewidth = 2)
plt.legend()
plt.show()