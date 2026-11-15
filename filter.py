numbers = [1, 2, 3, 4, 5, 6]#filter even numbers
result=filter(lambda number: number % 2==0, numbers)
print(list(result))

numbers = [1, 2, 3, 4, 5, 6]#filter odd  numbers
result=filter(lambda number: number % 2!=0, numbers)
print(list(result))

numbers = [1, -10, 2 , -25, 10]# filter positive number
result=filter(lambda number: number>0, numbers)
print(list(result))

#filter with strings
names = ["fatima", "faiza", "zaryab", "aman", "fara"]
result = filter(lambda name: name.startswith("f"), names)
print(list(result))

names = ["fatima", "faiza", "zaryab", "aman", "fara"]
result = filter(lambda name: len (name)>5, names)
print(list(result))

emails=["fatima@gmail.com", "invalid-email"]
result=filter(lambda email: "@" in email and "." in email.split("@")[-1], emails
)
print(list(result))


from functools import reduce
numbers= [10, 20, 30, 40]
result=reduce(lambda a,b: a+b,numbers)
print(result)

from functools import reduce
numbers= [10, 20, 30, 40]
result=reduce(lambda a,b: a*b,numbers)
print(result)


from functools import reduce
numbers= [10, 20, 80,  10, 30, 40]
result=reduce(lambda a,b: a if a>b else b,numbers)
print(result)

from functools import reduce
numbers= [10, 20, 30, 40]
result=reduce(lambda a,b: a+b,numbers,100)
print(result)

from functools import reduce
words= ["python", "is", "powerful"]
result=reduce(lambda a,b: a+"   "+b, words)
print(result)

# square even numbers and calculate their sum
from functools import reduce

numbers=[1, 2, 3, 4, 5, 6, 7, 8]
even_numbers=filter(lambda number: number % 2==0,numbers)

squared_numbers=map(lambda number: number**2, even_numbers)

total=reduce(lambda a,b: a+b,squared_numbers,0)

print("total", total)

#calculate total price of eligible products
products=[
   { "name": "laptop", "price":50000, "available":True},
   {"name":"mouse", "price":500, "available":True},
   {"name":"keyboard", "price":1200, "available":False},
   {"name":"monitor", "price":12000, "available":True}
]
available_products=filter(lambda product: product["available"],products)

prices=map(lambda product: product["price"],available_products)

total=reduce(lambda a,b: a+b, prices,0)

print("Total product available value:", total)
