
arr3=np.array([10,20,30,40,50,60,70,80,90,100])
print(arr3)

sliced= arr3[2:7].copy()
print(sliced)

sliced[4]=9999
print(sliced)  # Modified sub-array
print(arr2)  