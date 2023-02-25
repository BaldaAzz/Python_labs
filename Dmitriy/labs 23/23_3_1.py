import numpy as np

lst = np.array(np.arange(8).reshape(8,1),int)
print(lst)
lst[1] = -8
print(2 in lst)
lst2 = lst.reshape(2,4)
print(lst2)
print(lst.shape)
