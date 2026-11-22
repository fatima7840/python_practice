from studentmanagement.operations import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_students
)

from studentmanagement.reports import(
    class_statistics)

while True:
    print("student management system")

    print("1. add a student")
    print("2. view all students")
    print("3. search for a student")
    print("4. update student marks")
    print("5. delete a student")
    print("6. calculate class statistics")
    print("7. exit")

    choice =input("enter your choice:").strip()
    if choice =="1":
            add_student()
    elif choice =="2":
            view_students()
    elif choice =="3":
            search_student()
    elif choice =="4":
            update_student()
    elif choice =="5":
            delete_students()
    elif choice =="6":
            class_statistics()
    elif choice =="7":
            print("thank you!")
            break
    else:
            print("invalid choice. please try again.")
