import numpy as np
import matplotlib.pyplot as plt

# Define the rect function
def rect(t):
    return np.where(np.abs(t) < 0.5, 1, 0)

# Define the time range for the plot
t = np.linspace(-10, 10, 1000)

# Calculate the values of x_1(t)
x_1 = rect(t/3)

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(t, x_1, label='x_1(t) = rect(t/3)')
plt.xlabel('t')
plt.ylabel('x_1(t)')
plt.legend()
plt.grid(True)
plt.savefig('gate_x1.png')
plt.show()

