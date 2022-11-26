import pandas as pd
import numpy as np

arr = np.array([1, 6, 8, 3])

# Series is a one-dimensional labeled array
arr2 = pd.Series(arr)
arr1 = pd.Series(arr, index=['a', 'b', 'c', 'd'])

print(arr1)
print(arr2)
print(arr2[:2])

print(arr1[0])
print(arr1["c"])

user = {
    "name": "Suyash",
    "age": 20
}
obj_series = pd.Series(user)
print(obj_series)
print(obj_series[0])
print(obj_series["age"])

user_matrix = [
    ["Suyash", 20],
    ["Shubham", 25],
    ["Ananya", 19]
]
df1 = pd.DataFrame(user_matrix, index=[1, 2, 3], columns=["Name", "Age"])
print(df1)

users_data = {
    "name": ["Anshuman", "Sandeep", "Yashas"],
    "age": [20, 21, 21]
}

df2 = pd.DataFrame(users_data, index=["Friend 1:", "Friend 2:", "Friend 3:"])
print(df2)