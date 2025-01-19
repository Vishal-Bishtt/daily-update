import sympy as sp

# Define the symbols
x, y = sp.symbols('x y')

# Define the function u
define_u = sp.exp(x) * (x * sp.cos(y) - y * sp.sin(y))

# Compute the second partial derivatives
Uxx = sp.diff(define_u, x, x)
Uyy = sp.diff(define_u, y, y)

# Verify Uxx + Uyy = 0
laplace_result = Uxx + Uyy

# Display the results
print("Uxx:", Uxx)
print("Uyy:", Uyy)
print("Uxx + Uyy:", laplace_result)

# Check if the result is zero
if sp.simplify(laplace_result) == 0:
    print("The function satisfies the Laplace equation Uxx + Uyy = 0.")
else:
    print("The function does NOT satisfy the Laplace equation Uxx + Uyy = 0.")
