import numpy as np

lst = np.array(np.arange(-5,10),int)
lst_copy = lst.copy()
neg = lst < 0
negative = np.delete(lst.copy, neg)
print((negative))