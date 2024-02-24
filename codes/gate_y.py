import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if x < -4.5:
        return 0
    elif -4.5 <= x < -2.5:
        return 1
    elif -2.5 <= x < -1.5:
        return x + 3.5
    elif -1.5 <= x < -0.5:
        return x + 2.5
    elif -0.5 <= x < 0.5:
        return 2
    elif 0.5 <= x < 2.5:
        return -x + 4.5
    elif 2.5 <= x < 3.5:
        return 2
    else:
        return 0

x_values = np.linspace(-6, 6, 1000)
y_values = np.array([f(x) for x in x_values])

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.savefig('gate_y.png')
plt.show()

