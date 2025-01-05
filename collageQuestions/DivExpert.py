def DicExp(a,b):
    if a<0:
        print("first integer cannot be less than zero!!")
    else:
        if b==0:
            print("Error. Stack Overflow")
        else:
            c=a/b
    return c
num1 = int(input("Enter first integer: "))
num2= int(input("Enter second integer: "))
print(DicExp(num1,num2))