import numpy as np
numbers=np.array([10, 20, 30, 40, 50])
print(numbers)

matrix=np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(matrix)

data=np.array([
    [[1, 2],
    [3, 4]],
    [[5, 6],
     [7, 8]]
])
print(data)

marks=[85,90, 75, 88]
array_marks=np.array(marks)
print(array_marks)

numbers=np.array([10, 20, 30, 40, 50])
print("array:",numbers)
print("dimensions:",numbers.ndim)
print("shape:", numbers.shape)
print("size:", numbers.size)
print("data type:", numbers.dtype)

matrix=np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("dimensions:",matrix.ndim)
print("shape:", matrix.shape)
print("size:", matrix.size)

integers=np.array([10, 20, 30])
decimal=np.array([10.3, 20.5, 30.00])
characters=np.array(["A", "B", "C"])
boolean=np.array([True, False, True])
print(integers.dtype)
print(decimal.dtype)
print(characters.dtype)
print(boolean.dtype)

numbers=np.array([10, 20, 30, 40], dtype=np.float64)
print(numbers)
print(numbers.dtype)

numbers=np.array([10.5, 50.55, 20.333], dtype=np.int64)
print(numbers)
print(numbers.dtype)

numbers=np.array([10.8, 20.5, 30.9])
integers_numbers=numbers.astype(int)
print(integers_numbers)

numbers=np.array([10, 20, 50])
decimal=numbers.astype(float)
print(decimal)