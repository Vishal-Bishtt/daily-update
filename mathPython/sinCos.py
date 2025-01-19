import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x = np.linspace(0, 2 * np.pi, 500)

# Compute the sine and cosine values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y_sin, label='sin(x)', color='blue')
plt.plot(x, y_cos, label='cos(x)', color='red')

# Add labels, title, and legend
plt.xlabel('x values (radians)')
plt.ylabel('y values')
plt.title('Sine and Cosine Curves')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
