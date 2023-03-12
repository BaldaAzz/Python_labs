import numpy as np

array = np.array(np.arange(8),int)

print("исходный массив:",array)

array[1] = -8
array = array.reshape(2,4)

print("в масиве есть 2:",2 in array)
print("измененный масив:\n",array)
print("строк",array.shape[0],"\nстолбцев",array.shape[1])
