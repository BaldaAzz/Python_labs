import numpy as np

lst = np.array(np.arange(8),int)

print("исходный массив:",lst)

lst[1] = -8
lst = lst.reshape(2,4)

print("в масиве есть 2:",2 in lst)
print("измененный масив:",lst)
print("строк",lst.shape[0],"\nстолбцев",lst.shape[1])
