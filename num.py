import numpy as np
numbers=[10, 20, 30, 40]
print(type(numbers))
print(numbers)
result=np.array(numbers)
print(result)
print(type(result))

numbers=[12, 35, 50, 20]
numbers=np.array(numbers)
result=(numbers*2)
print(result)

numbers=[3, 6, 8, 15]
numbers=np.array(numbers)
result=(numbers**3)
print(result)

print(np.__version__)





