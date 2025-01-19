import sympy as sp

x, y = sp.symbols('x,y')
e = sp.exp(x)*(x*sp.cos(y)*y*sp.sin(y))
Uxx= sp.diff(e,x,x)
uyy = sp.diff(e,y,y)
result = Uxx+uyy
print("Uxx: ",Uxx)
print("Uyy: ",uyy)
print("Result: ",result)
if sp.simplify(e)==0:
    print("The fuction sestisfies the laplace equation ")
else:
    print("The equation does not sestisfies the laplace equation")