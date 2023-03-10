import numpy as np

array = np.random.randint(-50, 50, (8, 9))
array.flatten()

min = np.argmin(array)
max = np.argmax(array)
array[min], array[max] = array[max], array[min]
array.reshape(8, 9)

print("индекс минимального элемента:",min,' \n индекс макимального элемента',max)
print(array)
