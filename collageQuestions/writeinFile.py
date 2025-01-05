with open("newFile",'w') as f:
    a = input("Enter the text you want to write in file: ")
    f.write(a)
    f.flush()
    f.close()