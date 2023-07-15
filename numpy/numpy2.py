import numpy as np

arr = np.array([[1,2,3,5],[4,5,6,8],[7,8,9,12]], dtype = np.float32)
#print(arr)

newArr = arr.reshape(4,3)
print(newArr.ndim)
print(newArr)