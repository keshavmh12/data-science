import numpy as np

arr= np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(arr)

print(np.sum(arr, axis=0))  # Sum of each column
print(np.sum(arr, axis=1))  # Sum of each row

#indexing in multidimention array

#You can access elements using row and column indices.
print(arr[1,2])  # Element at 2nd row, 3rd column
print(arr[1,1])

#You can access elements using row and column indices.
print(arr[0:2,1:3])  # Sub-array from 1st and 2nd rows, 2nd and 3rd columns])
print(arr[1:,0:2])  # Every other row and column


#Indexing in 3D Arrays
arr3D = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[7, 8, 9], [10, 11, 12]]])

# Output of arr3D.shape is → (depth, rows, columns)
print(arr3D.shape)  # Output: (2, 2, 3) 

print(arr3D[0,1,2])  # Output: 6
print(arr3D[1,0,2]) # Output: 9


# Get all rows of the first column
first_col = arr[:, 0]
print(first_col)  # Output: [1 4 7]

# Get all rows of the first column
first_col = arr[:, 0]
print(first_col)  # Output: [1 4 7]

# Get all columns of the second row

#1st row 
second_row = arr[0, :]
print(second_row)  # Output: [4 5 6]

# Get the first row from each "sheet" in a 3D array
first_rows = arr3D[:, 0, :]
print(first_rows)



