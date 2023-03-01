import numpy as np

lst = np.array(np.arange(-18,18).reshape(6,6),float)
row = lst[-2:]
lst[0].fill(0)

print(row,"\n////////////////////////////////////")
print(lst)
print("длинна",len(lst))