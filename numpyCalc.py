import numpy as np

a = np.array([10,20,30,40])
b = np.arange(4)

c = a - b
print(c)
c = b**2
print(c)
print(c==1)

##
Arr = np.array([[1,2],[3,4]])
print(Arr)
Brr = b.reshape(2,2)
print(Brr)
Crr = Arr*Brr
print(Crr)
Drr = np.dot(Arr, Brr)
###

Rmat = np.random.random((2,4))
print(Rmat)
print(np.sum(Rmat, axis = 1))
print(np.min(Rmat, axis = 0))
print(np.max(Rmat, axis = 1))
