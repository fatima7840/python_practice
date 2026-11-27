# axis in numpy
import numpy as np
marks=np.array([
    [80, 90, 85],
    [70, 75, 80],
    [90, 95, 92]
])
print("column totals:")
print(np.sum(marks, axis=0))

print("rows totals:")
print(np.sum(marks, axis=1))

average=np.mean(marks, axis=1)
print(average)

# broadcasting in numpy

numbers=np.array([10, 20, 30])
result=numbers+5
print(result)

matrix=np.array([
    [10, 20, 30],
    [40, 50, 60]
])
values=np.array([5, 10, 4])
result=matrix+values
print(result)

# filtering arrays using conditions

marks=np.array([35, 45, 67, 89, 92, 28])
passed=marks[marks>=40]
print(passed)

marks=np.array([35, 45, 67, 89, 92, 28])
result=marks[(marks>=40)&(marks<=80)]
print(result)

marks=np.array([35, 45, 67, 89, 92, 28])
marks[marks<=40]=0
print(marks)

# random numbers using numpy

rng=np.random.default_rng(seed=42)
numbers=rng.integers(1,101,size=5)
print(numbers)

numbers=rng.random(5)
print(numbers)

matrix=rng.integers(1, 10, size=(3, 3))
print(matrix)

numbers=np.array([1, 2, 3, 4, 5])
rng.shuffle(numbers)
print(numbers)

# matrix operations
# matrix addition
a=np.array([
    [1, 2],
    [3, 4]
])

b=np.array([
    [5, 6],
    [6, 7]
])
print(a+b)

# matrix multiplication
a=np.array([
    [1, 2],
    [3, 4]
])

b=np.array([
    [5, 6],
    [6, 7]
])
print(a@b)


