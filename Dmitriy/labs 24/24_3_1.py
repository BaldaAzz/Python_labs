import numpy as np

array1 = np.array(np.arange(-18, 18).reshape(6, 6),int)
array2 = np.prod(array1, axis=0)
min = np.argmin(array2)

print(array1)
print(array2)
print(min)
