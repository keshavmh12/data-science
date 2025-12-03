import numpy as np

# Indexing
arr = np.array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18]
])
print(arr)

flat = arr.flatten()
print(flat)

print(flat[2])
print(arr[:3])
print(arr[::2])

# Slicing returns a VIEW
arr2 = np.array([10,20,30,40,50,60,70,80,90,100])
print(arr2)

sliced = arr2[2:7]
print(sliced)

sliced[4] = 9999
print(sliced)
print(arr2)

# Use .copy() to avoid modifying original
arr3 = np.array([10,20,30,40,50,60,70,80,90,100])
print(arr3)

sliced = arr3[2:7].copy()
print(sliced)

sliced[4] = 9999
print(sliced)
print(arr3)

# Fancy indexing & Boolean masking
arr4 = np.array([10,20,30,40,50,60,70,80,90,100])
idx = [1,3,5,7]
fancy = arr4[idx]
print(fancy)

mask = arr4 > 25
masked = arr4[mask]
print(masked)
