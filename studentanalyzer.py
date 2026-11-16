# student performance analyzer
from functools import reduce

students=[{"name":"fatima", "marks":[85, 90, 80]},
          {"name":"maryam","marks":[70, 75, 80]},
          {"name":"aman","marks":[95, 92, 98]},
          {"name":"rani", "marks":[30, 40, 45]}]

def calculate_total(student):
    return sum(student["marks"])

def calculate_average(student):
    return calculate_total(student)/len(student["marks"])

def assign_grades(average):
    if average>=85:
        return "A"
    elif average>=70:
        return "B"
    elif average>=50:
        return "C"
    else:
        return "fail"

def generate_report():
    student_reports=list(map(lambda student:{
        "name":student["name"],
        "total":calculate_total(student),
        "average":calculate_average(student),
        "grade":assign_grades (calculate_average(student))}, students))


    #filter passed students
    passed_student=list(filter(lambda student:student["grade"]!="fail",student_reports))

    #filter failed students
    failed_student=list(filter(lambda student:student["grade"]=="fail",student_reports))

    #sort student by aqverage marks
    ranked_students=sorted(student_reports, key =lambda student:student ["average"],reverse=True)

    # calculate class average
    class_total=reduce(lambda total, student: total+student["average"],student_reports,0)
    class_average=class_total/len(student_reports)

    #display report
    print("=========STUDENT PERFORMANCE ANALYZER==========")

    for student in ranked_students: 
        print(
            student["name"],
              "Total:",student["total"],
              "average:",student["average"],
              "grade:",student["grade"]
              )

    print("passed students:", len(passed_student))
    print("failed students:", len(failed_student)) 
    print("class average:", round(class_average,2))
    print("topper:", ranked_students[0]["name"])

generate_report()