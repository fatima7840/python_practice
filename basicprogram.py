n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    print("sum of natural number is:",sum)
table=int(input("enter your number:"))
for i in range(1,11):
    print(f"{table}x{i}={table*i}")