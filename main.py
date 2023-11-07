import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x) * np.cos(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('log(x) + cos(x)')
plt.title('График функции log(x) + cos(x)')
plt.grid(True)
plt.show()

