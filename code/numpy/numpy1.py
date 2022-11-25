import numpy as np

# most important object defined in NumPy is an N-dimensional array type called ndarray.
# Each element in ndarray is an object of data-type object (called dtype)

# Datatype of each element is by-default int64
arr = np.array([
    [2, 3, 2,],
    [9, 3, 1],
    [0, 2, 6]
])
print(arr.shape)
print(arr.size)
print(type(arr)) # numpy.ndarray
print(type(arr[1][2])) # numpy.int64
# Reshape the 3 row 3 columns into 1 row 9 columns
print(arr.reshape(1, 9))
# Cannot reshape the 3 by 3 matrix into 4 by 2. So, error will be thrown
# print(arr.reshape(4, 2))

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
# Reshape the 3 rows 2 columns into 2 columns 3 rows
print(arr2.reshape(3, 2))
# Resize can transform a m by n into an x by y matrix
# It starts filling the vacant positions by repeating the elements from the start once the elements of original matrix are exhausted
print(np.resize(arr2, (3, 3)))
# It drops the elements if the number of elements from the original matrix are more than available positions in the newly formed matrix
print(np.resize(arr2, (1, 4)))

# np.arange(start, stop, step, dtype)
# dtype is by-default of type int64
# 10 and 15 will be printed
# 20 is not inclusive
print(np.arange(10, 20, 5))
print(np.arange(1, 10, 10)) # 1
arr3 = np.arange(-100, 100, 50).reshape(2, 2) # [[-100, -50], [0, 50]]
print(arr3)
arr4 = np.arange(1, 21, 1, dtype=np.int8)
print(arr4)
print(type(arr4[0]))
# Short way to use arange
# Values start from 0
print(np.arange(5))

# Dimensions
print(arr4.ndim)
print(arr3.ndim)
# Creating a 4-dimensional matrix 2x2x2x3
arr5 = np.arange(24).reshape(2, 2, 2, 3)
print(arr5.ndim)