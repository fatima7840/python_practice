task 1 :type conversion
num=float(45)
print(num)
num=int(99.999)
print(num)
number=input("enter a number:")
a=int(number)
print(a)
print(type(a))
fruits=["apple", "banana", "cherry"]
a=tuple(fruits)
print(a)
flowers=("rose", "lily", "lotus")
a=list(flowers)
print(a)

# task 2 :operators
number=int(input("enter a number:"))
if number % 2==0:
    print("even")
else:
    print("odd")

name=["fatima", "sana", "maria", "maryam"]
if "fatima" in name:
    print("name is present")
else:
     print("name is not present")
     
age=int(input("enter your age:"))
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote") 

a=10
b=20
a+=b
a*=2  
print(a)  

operations in datatypes
a="hello"
b="python"
print(a+" "+b)

a=20
b=35
print(a+b)

a="hello"
b=4
print(a*b)

list1=[10,20,30]
list2=[1,2,3]
print(list1+list2)

name="python"
print(name[0:6:2])
print(name[::-1])

numbers=[10,20,30,40,50]
print(numbers[0:4])
print(numbers[2:4])

# real life input and output
name=input("enter a name:")
print(name)
age=int(input("enter your age:"))
print(age)
marks=float(input("enter your marks:"))
print(marks)
print(f"my name is {name},{age},{marks}")

# task 5:if-else
nums=int(input("enter a nums:"))
if nums % 2==0:
    print("even number")
else: 
    print("0dd number")

marks=float(input("enter your marks:"))
if marks >=90:
    print("grade A")
elif marks >=75:
    print("grade B")
elif marks >=60:
    print("grade C")
elif marks >=35:
    print("grade D")
else:
    print("fail")  

age=int(input("enter your age:"))
if age>=18:
    print("eligible for vote")  
else:
    print("not eligible for vote")   

password=input("enter your password:")
if password == "123490":
    print("correct password")
else:
    print("incorrect password")                                

a=int(input("enter a number:"))
b=int(input("enter a number:"))
if a>b:
    print("a is greatest")
elif b>a:
    print("b is the greatest")  
else:
    print("both are equal")  

#task 5: for loop
fruits=["persimon", "blackberry", "cherry"]
for fruit in fruits:
    print(fruit)
    for i in fruit:
        print(i)

name=input("enter a name:")
count=0
for i in name:
    count+=1
print("the total is",count)   


          