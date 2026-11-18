import math
print(math.sqrt(64))
print(math.pow(2,4))
print(math.ceil(5.9))
print(math.floor(3.4))
print(math.factorial(8))
print(math.fabs(-23))
print(math.fabs(35))
print(math.gcd(21,35))
print(math.pi)
print(math.e)

#circle calculator
radius=float(input("enter circle radius:"))
area=math.pi * radius **2
circumference=2*math.pi*radius
print("area:",round(area,2))
print("circumference:",round(circumference,2))