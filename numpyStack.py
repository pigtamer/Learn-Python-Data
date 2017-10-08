import numpy as np
split = "-"*20

A = np.array([1,1,1])
B = np.array([2,2,2])
split
print(A)
print(B)
AvB = np.vstack((A,B))
AhB = np.hstack((A,B))

print(AvB)
print(AhB)
print(np.vstack((AvB, A)))
split
AcB = np.concatenate((A,B,B,A),axis=0)
print(AcB)

split
print(A[:, np.newaxis])
print(A[np.newaxis, :])
