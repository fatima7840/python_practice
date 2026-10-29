n=int(input("enter a number:"))#tsum of natural numbers
value=0
for i in range(1,n+1):
    value+=i
print("the sum of natural number is:",value)

#nestedloops
flowers=["rose", "lily", "lotus", "jasemine"]
for flower in flowers:
    count=0
    print(flower)
    for i in flower:
        count+=1
        print(i)
    print("the number of letters in flower name is:",count)
     
#ifelse
a=15
b=25
c=20
if a>b and a>c:
    print("a is the greatest")
elif b>a and b>c:
    print("b is the greatest")
else:
    print("c is the greatest")  

age=21
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")

#program
value=[15, 20, 15, 5]  
total=0
for i in value:
    total+=i
print("the total is:",total)
if total>50:
    print("ypu are eliginle for discount")
else:
    print("you are not eligible for discount")






