import sympy as sp

# Define the variable x
x = sp.symbols('x')

# Define the expression
expression = (1 + 1 / x)**x

# Compute the limit as x approaches infinity
limit_value = sp.limit(expression, x, sp.oo)

# Display the result
print("The limit of (1 + 1/x)^x as x approaches infinity is:", limit_value)
