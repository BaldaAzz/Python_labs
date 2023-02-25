import numpy as np

lst = np.array(np.arange(-18,18).reshape(6,6),float)
row = lst[-2:]
print(row,"\n////////////////////////////////////")
lst[0].fill(0)
print(lst)
print("длинна",len(lst))