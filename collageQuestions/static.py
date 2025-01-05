from math import sqrt
myList=[]
len = int(input("Enter the number of elements you want to enter in list: "))
for i in range(0,len):
    a= int(input("Enter your element: "))
    myList.append(a)
Total = 0
for i in myList:
    Total+=i
mean = Total/len
print("Mean: ",mean)
total = 0
for ele in myList:
    total+=(ele-mean)*(ele-mean)
variance = total/len
sDaviation = sqrt(variance)
print("Variance: ",variance)
print("Standard: ",sDaviation)