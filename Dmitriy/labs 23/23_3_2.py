import numpy as np

array = np.array(np.arange(-18,18).reshape(6,6),float)
row = array[-2:]
array[0].fill(0)

print(row,"\n////////////////////////////////////")
print(array)
print("длинна",array.size)