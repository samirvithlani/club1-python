import numpy as np

#arr = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype = np.float32)
#print(arr)
#arr = np.zeros((3,4))
#arr = np.ones((3,4))
#arr = np.full((3,4), 5)
#arr =np.arange(10,25,5)
np.random.seed(1)
arr = np.random.randint(0,100,5)
print(arr)
print("array is of type: ", type(arr))
print("No. of dimensions: ", arr.ndim)
print("Shape of array: ", arr.shape)
print("Size of array: ", arr.size)
print("Array stores elements of type: ", arr.dtype)