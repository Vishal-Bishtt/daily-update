def facorial(a):
    f = 1
    for i in range(1,a+1):
        f *=i
        print(f)
    print(f)
    return f
n=int(input("Enter the value of N : "))
r =int(input("Enter the value of R (R cannot be negitive or gretar than N): "))
nCr=facorial(n)/(facorial(r)*facorial(n-r))
print("nCr = ",nCr)

