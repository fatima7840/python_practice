import random
print(random.randint(1,10))
print(random.randrange(1,25,3))
print(random.random())
print(random.uniform(10,34))
colors=['red', 'blue', 'green', 'pink']
print(random.choice(colors))
colors=['red', 'blue', 'green', 'pink']
print(random.choices(colors,k=2))
numbers=[10, 20, 30, 40,50]
print(random.sample(numbers,k=4))
numbers=[10, 20, 30, 40, 50]
random.shuffle(numbers)
print(numbers)
random.seed(12)
print(random.randint(1,35))
print(random.randint(1,35))

#dice simulator
import random
while True:
    input("press enter to roll the dice")
    dice=random.randint(1,6)
    print("dice result:", dice)
    choice=input("roll again?(yes/no):")
    if choice!="yes":
        print("game finished")
        break
