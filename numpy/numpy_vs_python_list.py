import numpy as np
import time

#python list
size=1000000
list1 =list(range(size))
list2 =list(range(size))

start=time.time()
result = [x + y for x,y in zip(list1,list2)]
end=time.time()
print(f"pythin list addition time",end-start)

#numpy array
array1=np.array(list1)
array2=np.array(list2)

start=time.time()
result= array1 + array2
end=time.time()
print(f"numpy array addition time",end-start)


#memory efficiency
list_data = list(range(1000))
numpy_data = np.array(list_data)

print("python list memory size:",sys.getsizeof(list_data)) 
len((list_data),"bytes")
print("numpy array memory size:",numpy_data.nbytes,'bytes')

