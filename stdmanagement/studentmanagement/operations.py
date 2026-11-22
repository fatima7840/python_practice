students = {}
def add_student():

    student_id =input("enter student ID:").strip()

    if not student_id:
        print("student_id cannot be empty.")
        return
    
    if student_id in students:
        print("student_id already exits.")
        return
    
    name =input("enter student name:").strip()

    if not name:
        print("name cannot be empty.")
        return
    
    try:
        marks =float(input("enter marks:"))

        if not 0 <= marks <= 100:
            print ("marks must be between 0 and 100")
            return
        
    except ValueError:
        print("marks must be numeric.")
        return
    
    students[student_id] = {
        "name": name,
        "marks":marks
    }

    print("student added successfully") 
    



def view_students():

    if not students:
        print("no students records found")
        return

    for student_id, details in students.items():
        print("student id:", student_id)
        print("name:", details["name"])
        print("marks:", details["marks"])




def search_student():
    student_id =input("enter student id:").strip()
    student =students.get(student_id)

    if student is None:
        print("student not found")
        return
    print("student found")
    print("name:", student["name"])
    print("marks:", student["marks"])
   


def update_student():
    student_id =input("enter student id:").strip()

    if student_id not in students:
        print("student not found")
        return
    try:
        marks=float(input("enter your marks:"))
        if not 0 <= marks <=100:
            print("marks must be  between 0 to 100")
            return

    except ValueError:
        print("invalid marks")  
        return

    students[student_id]["marks"] =marks
    print("marks updated successfully.")  



def delete_students():
    student_id =input("enter student id:").strip()

    if student_id not in students:
        print("student not found")
        return

    confirm =input("confirm delete? (yes/no):").strip().lower()
    if confirm == "yes":
        del students[student_id]
        print("student deleted successfully.")
    else:
        print("deletion cancelled.")
 

