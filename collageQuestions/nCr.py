def facorial(a):
    if a==0:
        return 1
    else:
        return a*facorial(a-1)
n=int(input("Enter the value of N : "))
r =int(input("Enter the value of R (R cannot be negitive or gretar than N): "))
nCr=facorial(n)/(facorial(r)*facorial(n-r))
print("nCr = ",nCr)

