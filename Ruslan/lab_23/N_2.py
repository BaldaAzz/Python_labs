import numpy as np 
from random import randint


a = [randint(-10, 10) for i in range(42)]


arrray_1 = np.array(a, dtype=int)

arrray_1 = arrray_1.reshape(6, 7)
print(arrray_1)

print(arrray_1[0])

print(-arrray_1[0])

print(arrray_1.size)