import os
print(os.getcwd())
print(os.listdir())
os.mkdir("fp")
print("folder created")
os.makedirs("project/data/report",exist_ok=True)
print("directories created")
path="new folder"
if os.path.exists(path):
    print("path exists")
else:
    print("path does not exist")   

path="filter.py"    
if os.path.isfile(path):
    print("it is a file")
elif os.path.isdir(path):
    print("it is a directory")  
else:
    print("path mot found") 

os.rename("calc.py", "calcy.py") 

os.rmdir("new folder")    

username=os.getenv("username","unknown")
print(username)

os.system("echo hello from python")


