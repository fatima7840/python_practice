from studentmanagement.operations import students

def class_statistics():
    if not students:
        print("no students records available.")
        return

    marks =[student["marks"]for student in students.values()]

    total =sum(marks)
    average =total/len(marks)
    highest =max(marks)
    lowest =min(marks)

    print("class statistics")

    print("total students:",len(students))
    print("total marks:",total)
    print("average marks:",round(average,2))
    print("highest marks:",highest)
    print("lowest marks:",lowest)