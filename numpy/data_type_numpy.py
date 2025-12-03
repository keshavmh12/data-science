import numpy as np

arr=np.array([1,2,3,4,5])
print(arr.dtype)

#2. Changing Data Types

arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr.dtype)  # Output: int64 (or int32 depending on the system)

arr_int=arr.astype(np.int32)
print(arr_int.dtype)  # Output: int32

#Example: Downcasting to Save Memory
arr_large = np.array([1000000, 2000000, 3000000], dtype=np.int64)
arr_small = arr_large.astype(np.int32)  # Downcasting to a smaller dtype
print(arr_small)  # Output: [1000000 2000000 3000000]
print(arr_small.dtype)  # Output: int32

#Example: Complex Numbers
arr = np.array([1 + 2j, 3 + 4j, 5 + 6j], dtype='complex128')
print(arr)