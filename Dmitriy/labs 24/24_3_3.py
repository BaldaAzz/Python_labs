import numpy as np

lst = np.array(np.arange(12).reshape(1,12),int)
lst = lst.reshape(3,4)
print(lst,"\n///////////////////////")
np.fill_diagonal(np.fliplr(lst), -1) 
print(lst)
