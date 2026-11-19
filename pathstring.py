from pathlib import Path
current_folder= Path.cwd()
print(current_folder)
file_path=Path("data")/"student.txt"
print(file_path)
path=Path("student.txt")
print(path.exists())
path=Path("data")
print(path.exists())
path=Path("student.txt")
if path.is_file():
    print("file found")
elif path.is_dir():
    print("directory found")
else:
    print("path not found")  

folder=Path("reports")   
folder.mkdir(exist_ok=True)
print("folder created")
file_path=Path("reports/student_marks.pdf")  
print(file_path.name)
print(file_path.stem)
print(file_path.suffix) 

folder=Path(".")
for file in folder.iterdir():
    print(file)

for file in Path(".").glob("*.py"):
    print(file)   

    

