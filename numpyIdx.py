import numpy as np
A= np.arange(3,15).reshape((3,4))

print(A)
print(A.flatten()) #does not return

print(A[2][1])
print(A[:][1]) # all in row 2
print(A[:][0])
print(A[1][1:3])
print('-' *20)

for item in A.flatten():
    print(item)
print('-' *20)

for column in A.T:
    print(column)
print('-' *20)
for rows in A:
    print(rows)
