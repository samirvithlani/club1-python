import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

arr.sort(axis=1)
print(arr)

sum  = arr.sum()
sum1 = arr.sum(axis=0)
sum2 = arr.sum(axis=1)
print(sum)
print(sum1)
print(sum2)

# arr = arr.transpose()
# print(arr)
arr = arr.T
print(arr)