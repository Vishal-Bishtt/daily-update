num = input("Enter your number: ")
print("The number entered is: ",num)
#se = set(num)
for i in num:
    print(i," occures ",num.count(i)," times.")