import numpy as np

lst = np.array(np.arange(-18,18).reshape(6,6),int)
lst2 = np.prod(lst, axis = 0)

print(lst2)
print(min(lst2))
