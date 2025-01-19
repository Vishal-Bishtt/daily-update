import numpy as np

# Define the matrix
a = np.array([
    [4, 3, 2],
    [1, 4, 1],
    [3, 10, 4]
])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(a)

# Find the largest eigenvalue
largest_eigenvalue = np.max(eigenvalues)

# Display the result
print("Eigenvalues:", eigenvalues)
print("Largest Eigenvalue:", largest_eigenvalue)
