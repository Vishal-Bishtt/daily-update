import numpy as np
import matplotlib.pyplot as plt

# Define the range of theta values
theta = np.linspace(0, 2 * np.pi, 1000)

# Define the polar function r = 2|cos(2*theta)|
r = 2 * np.abs(np.cos(2 * theta))

# Create the polar plot
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)
ax.plot(theta, r, label=r"$r = 2|\cos(2\theta)|$", color='blue')

# Add title and legend
ax.set_title("Polar Plot of r = 2|cos(2*theta)|", va='bottom')
ax.legend(loc='upper right')

# Show the plot
plt.show()
