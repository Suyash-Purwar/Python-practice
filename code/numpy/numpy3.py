import numpy as np
import math

arr1 = np.array([
    [4, 3, 19],
    [7, 6, 3],
    [3, 7, 2]
])

arr2 = np.array([
    [2, 3, 1],
    [5, 3, 7],
    [3, 6, 2]
])
# Arithmetic Operations
print(np.add(arr1, arr2))
print(np.subtract(arr1, arr2))
print(np.multiply(arr1, arr2))
print(np.divide(arr1, arr2))

print(np.ptp(arr1)) # Finds the difference between the maximum and minimum value
print(np.ptp(arr1, axis=0)) # Finds the difference between the maximum and minimum value column-wise
print(np.ptp(arr1, axis=1)) # Finds the difference between the maximum and minimum value row-wise

# Median - Center value of the data
print(np.median(arr1))
print(np.median(arr1, axis=0))
print(np.median(arr1, axis=1))

# Mean - Arithmetic Mean of all the elements
# numpy.mean() computes normal avg
print(np.mean(arr2))
print(np.mean(arr2, axis=0))
print(np.mean(arr2, axis=1))

# numpy.average() computes the weighted average
# Consider an array [1, 2, 3, 4] which has weights [3, 4, 2, 4]
# Weight avg = (1*3+2*4+3*2+4*4) / (3+4+2+1)
vals = np.array([1, 2, 3, 4])
wts = np.array([3, 4, 2, 4])
print(np.average(vals, weights=wts))

# Standard Deviation
# Standard deviation is the square root of the average of squared deviations from mean.
# The formula for standard deviation is as follows − sqrt(mean(abs(x-x.mean())*2*))
print(np.std(arr2))
print(np.std(vals))

# Variance is the average of squared deviations, i.e., mean(abs(x - x.mean())**2).
# In other words, the standard deviation is the square root of variance.
print(np.var(vals))
print(math.sqrt(np.var(vals)) == np.std(vals))

arr3 = np.arange(1, 4)
print(arr3)
arr4 = np.array([
    [1, 2, 1],
    [2, 1, 2]
])
print(arr3 + arr1)
# print(arr4 + arr1) - NOT POSSIBLE