import numpy as np

array = np.array(np.arange(12),int)
array = array.reshape(3, 4)

print(array,"\n")

np.fill_diagonal(np.fliplr(array), -1) 

print(array)
