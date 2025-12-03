import numpy as np
#cover list to array

#1d array
arr=np.array([1,2,3,4,5])
print(arr)

#2d array
aar2 = np.array([[1,2,3],[4,5,6]])
print(aar2)

#creating array of zeros
zeros_array = np.zeros((3,4))
print(zeros_array)

#creating array of ones
ones_array = np.ones((2,5))
print(ones_array)

#creating array with specific value
full_array=np.full((6,7),78)
print(full_array)

#identity matrix
identity_matrix = np.eye(5)
print(identity_matrix)

#arrange function
arrange_array = np.arange(2,200,20)
print(arrange_array)

#evenly spaced array
evenly_spaced_array = np.linspace(0,7,6)
print(evenly_spaced_array)

#for find sape of array
arr_shape= aar2.shape
print("shape of array:",arr_shape)

#for find size of array
arr_size= aar2.size
print("size of array:",arr_size)

# find dimention of the array
arr_dimention = aar2.ndim
print("dimention of array:",arr_dimention)

#dfault datatype of array
default_dtype= arr.dtype
print("default datatype of array:",default_dtype)

# Changing Data Types

arr = np.array([1, 2, 3], dtype=np.float32)  # Explicit type
print(arr.dtype)  # float32

arr_int = arr.astype(np.int32)  # Convert float to int
print(arr_int)  # [1 2 3]

#Reshaping Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # (2, 3)

reshaped = arr.reshape((3, 2))  # Change shape
print(reshaped)
# [[1 2]
#  [3 4]
#  [5 6]]

flattened = arr.flatten()  # Convert 2D → 1D
print(flattened)  # [1 2 3 4 5 6]


