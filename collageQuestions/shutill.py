import shutil
fname = input("Enter your file name: ")
dpath = input("Enter the path of your file: ")
shutil.make_archive(fname,'zip',dpath)