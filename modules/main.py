from calculator import sub, add, multiply
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
user_input= int(input("1 for add 2 for sub 3 for multiply"))
if user_input==1:
    print (add(num1,num2))

elif user_input==2:
    print(sub(num1,num2))
    
else:
    print(multiply(num1,num2))







