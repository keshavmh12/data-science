import numpy as np

arr = np.array([1,2,3,4,5])
result = arr**2
print(result)  # Output: [ 1  4  9 16 25].dtype)  # Output: complex128


result = arr + 10

print(result)  # Output: [11 12 13 14 15]

# add two arr
arr1 = np.array([4,6,8,9,3])
arr2 = np.array([2,3,7,8,9])

result1 = arr1 + arr2 
print(result1)  # Output: [ 6  9 15 17 12]

# add two dff dimention arrays
arr3 = np.array([[23,45,67,89],[23,67,56,45]])
arr4= np.array([34,56,34,78])
result2 = arr3 + arr4
print(result2)


#normalization of data using broadcasting
data = np.array([[12,34,56,78,90],
                 [23,45,67,89,12],
                 [34,56,78,90,23]])

mean = data.mean(axis=0)
std = data.std(axis=0)
normalization = (data - mean) / std
print(normalization)