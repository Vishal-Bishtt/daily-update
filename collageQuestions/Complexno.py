class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a + self.b)
n = int(input("Enter your number: "))
if n>=2:
    a= complex(input("Enter first number: "))
    b=complex(input("Enter second number: "))
    a1=Complex(a,b)
    a1.add()
else:
    print("Number entered should be greater than two!!")  