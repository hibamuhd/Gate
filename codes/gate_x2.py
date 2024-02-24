import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def rect(t, t0, length):
    return np.where((t >= t0 - length/2) & (t <= t0 + length/2), 1, 0)

# Generate x values
t = np.linspace(-5, 5, 1000)

# Calculate y values
y3 = rect(t, 0, 2)

# Plot the functions
plt.arrow(-3, 0, 0, 1, head_width=0.1, head_length=0.1, fc='black', ec='black')
plt.arrow(2, 0, 0, 2, head_width=0.1, head_length=0.1, fc='black', ec='black')

# Modify the rect function
y4 = rect(t, 0, 0.5)
plt.plot(t, y4, label='rect(2t)')

plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('gate_x2.png')
plt.show()

