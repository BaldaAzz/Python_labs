import numpy as np


array_1 = np.array([1, 2, 3, 4, 5, 6], dtype=int)

array_1[0] = -array_1[0]
print(array_1)

print(5 in array_1)

array_2 = array_1.reshape(2, 3)
print(array_2)