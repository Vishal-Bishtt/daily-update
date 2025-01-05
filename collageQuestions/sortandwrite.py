fname=input("Enter the directory of you file: ")
l=[]
with open(fname,'r') as f:
    a= f.read()
sp= a.split()
for i in sp:
    l.append(i)
l.sort()
cname = input("Enter the name of new file you want to create: ")
with open(cname,'w') as x:
    for i in l:
        x.write(i)
print("New file created successfully")