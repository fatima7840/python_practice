# file=open("student.txt","w")
# file.write("welcome to python file handling")
# file.write("student name:fatima\n")
# file.write("course:python\n")
# file.close()
# file=open("student.txt","r")

with open("student.txt","a") as file:
    file.write("\ncity:mumbai")
    file.write("\nage:28")
