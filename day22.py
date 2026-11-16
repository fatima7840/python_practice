square = lambda number: number*number #square
print(square(8))

greet = lambda name: "hello " + name#with one argument
print(greet("fatima"))

cube = lambda number: number**3
print(cube(4))
print(cube(15))

add = lambda a,b: a+b#with multiple argument
print(add(10,20))

multiply = lambda a,b: a*b
print(multiply(10,20))

add = lambda a,b,c: a+b+c
print(add(10,20,30))

check_number = lambda number: "Even" if number% 2==0 else "odd" #conditional expressions
print(check_number(15))
print(check_number(20))

greater= lambda a,b: a if a>b else b
print(greater(20,10))

check_age = lambda age: "eligible" if age >18 else "not eligible"
print(check_age(23))

# lambda built in functions
numbers=[50,10,40,20,30]
result = sorted(numbers, key=lambda number: number)
print(result)

numbers=[25,13,15,34,21]
result = sorted (numbers, key=lambda number: number%10)
print(result)

students =[{"name":"fatima", "marks":75},{"name":"marya", "marks":80},{"name":"liza", "marks":70}]
result = sorted(students, key=lambda student: student["marks"])
for student in result:
    print(student)


students =[{"name":"fatima", "marks":75},{"name":"marya", "marks":80},{"name":"liza", "marks":70}]
top_student = max(students, key=lambda student: student["marks"]) 
print(top_student)  


#MAP
numbers = [1, 2, 3, 4, 5]
result = map(lambda number:number**2, numbers)
print(list(result))

names =["fatima", "marya", "liza"]
result = map(lambda name: name.upper(), names)
print(tuple(result))

numbers = [1, 2, 3, 4, 5]
result = map(lambda number:number+10, numbers)
print(list(result))

def calculate_square(number):
    return number**2
numbers =[2, 4, 6, 8]
result = map(calculate_square,numbers)
print(list(result))

num1=[10, 20, 30]
num2=[1, 2, 3]
result=map(lambda a,b: a+b, num1, num2)
print(list(result))

num1=[10, 20, 30]
num2=[1, 2, 3]
result=map(lambda a,b: a*b, num1, num2)
print(list(result))

numbers =(2, 4, 6, 8)
result = map(lambda number: number*5, numbers)
print(tuple(result))

characters= ["a", "b", "c"]
result=map(lambda character: character.upper(),characters)
print(list(result))


# apply discount using map()
prices=[1000, 2000, 3000, 4000]
discounted_prices=map(lambda price: price-(price*10/100),prices)
print(list(discounted_prices))

# average using reduce
from functools import reduce
marks=[80, 90, 75, 85]
total=reduce(lambda a,b: a+b, marks, 0)
average=total/len(marks)
print("total", total)
print("average", average)


#filter price
prices=[50000, 500, 1200, 12000]
result=filter(lambda price: price<10000,prices)
print(list(result))







    
    

