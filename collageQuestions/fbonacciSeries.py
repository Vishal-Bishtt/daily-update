num = int(input("Enter the number to which you want your fivonacci series: "))
firstTerm = 0
secondTerm = 1
print(firstTerm,secondTerm,end=" ")
for i in range(2,num):
    curTerm = firstTerm+secondTerm
    print(curTerm,end =" ")
    firstTerm=secondTerm
    secondTerm=curTerm