import numpy as np
import sys
#memory efficiency
list_data = list(range(1000))
numpy_data = np.array(list_data)

print("python list memory size:",sys.getsizeof(list_data))
len(list_data)

print("numpy array memory size:",numpy_data.nbytes,'bytes')