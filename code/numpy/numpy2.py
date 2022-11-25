import numpy as np

# Every element by-default occupies 8 bytes
# Data type of element is by-default in int64
arr0 = np.array([
    [1, 8, -5, 2],
    [9, 4, -7, 0]
])
print(arr0.itemsize)
# Every element occupies 2 bytes
arr1 = np.arange(5, dtype=np.int16)
print(arr1.itemsize)

# Creating empty marix of NxM size
# Garbage value is assigned to these elements
arr2 = np.empty([3, 2], dtype=np.int16)
print(arr2)
print(arr2.itemsize)

# Default data type of elements is float
arr3 = np.zeros(5)
print(arr3)
print(type(arr3[0])) # np.float64

print(np.zeros([2, 2], dtype=np.int8))

# Default data type of elements is float
print(np.ones(3, dtype=np.int16))
print(np.ones([2, 2]))

list1 = [5, 3, 4, -6, 2, 0]
numpy_arr = np.asarray(list1)
normal_arr = list(numpy_arr)
print(type(numpy_arr)) # numpy.ndarray
print(type(normal_arr)) # list

# np.linspace() divides the range 10 to 50 in 5 equal sizes
# np.linspace() always return array of type int64
arr4 = np.linspace(10, 50, 5)
print(arr4)
print(type(arr4[0]))

arr5 = np.array([
    [10, 20, 30],
    [40, 30, -50],
])
# axis = 0 does column-wise summation
print(np.sum(arr5, axis=0)) # 10+40, 20+30, 30+(-50)
# axis = 1 does row-wise summation
print(np.sum(arr5, axis=1)) # 10+20+30, 40+30+(-50)
# Finds maximum element column wise
print(np.amax(arr5, axis=0))
# Finds maximum element row wise
print(np.amax(arr5, axis=1))
# Finds minimum element column wise
print(np.amin(arr5, axis=0))
# Finds minimum element row wise
print(np.amin(arr5, axis=1))