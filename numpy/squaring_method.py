import numpy as np
list1=[2,3,4,5,6,7,8,9]
arr1=np.array(list1)


#python list(loop-based)
list_squares=[x **2 for x in list1]
print(list_squares)

#numpy(vectorized)
numpy_squares=arr1 ** 2
print(numpy_squares)
