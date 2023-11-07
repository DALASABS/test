import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x) * np.cos(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x) * cos(x)')
plt.title('График функции sin(x) * cos(x)')
plt.grid(True)
plt.show()

