import numpy as np
a=  np.arange(2,14).reshape(3,4)

print(a)
print(np.argmin(a)) #linear index min
print(np.argmax(a)) #linear index max
print(np.mean(a))
print(np.average(a))
print(a.mean())
print(np.median(a))
print(np.cumsum(a)) # chain summary
print(np.diff(a)) #difference
print(np.nonzero(a)) #two lists out: nonzero element x and y idx.
print(np.transpose(a))
a
print(a.T)
print(np.clip(a, 5,9)) #soft threshold, ele=5 if ele<5 elif ele=9 if ele>9
print(np.mean(a, axis=0))#axis=0: by rows. axis = 1, by cols
print(np.mean(a, axis=1))#axis=0: by rows. axis = 1, by cols
