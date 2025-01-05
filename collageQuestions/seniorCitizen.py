name = input("Please enter your name : ")
dob = int(input("Please enter your date of birth : "))
cyear = int(input("Enter your current year : "))
age = cyear-dob
if age>60:
    print("hello ",name)
    print("You are a seniorcitizon")
else:
    print("hello ",name)
    print("You are not a seniorcitizon")