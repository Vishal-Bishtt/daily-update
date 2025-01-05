class Student():
    def __init__(self,name,usn):
        self.name = name
        self.usn = usn
        self.mark=[]
        self.subject=[]
    def enterMarks(self):
        for i in range(3):
            sub = input("Enter subject: ")
            mark = int(input("Enter your marks %s of %s: "%(self.name,sub)))
            self.subject.append(sub)
            self.mark.append(mark)
    def total(self):
        tot = self.mark[0]+self.mark[1]+self.mark[2]
        return tot
    def per(self):
        percent = (self.mark[0]+self.mark[1]+self.mark[2])/3
        return percent
    def dis(self):
        print(self.name,"USN: ",self.usn," got ",self.mark," marks in ",self.subject," subjects")
        print("Total marks obtained: ",self.total())
        print("Percentage: ",self.per())
name = input("Enter the naem of student: ")
usn = input("Enter the usn of the student: ")
s1 = Student(name,usn)
s1.enterMarks()
s1.dis()