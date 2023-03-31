import numpy as np

array = np.random.randint(-50, 50, (8, 9))

print(array)

maximum = np.max(array)
minimum = np.min(array)
index_max_element = np.where(array == maximum)
index_min_element = np.where(array == minimum)

print("максимальный элемент",maximum)
print("минимальный элемент",minimum)

array[index_max_element[0][0], index_max_element[1][0]] = minimum
array[index_min_element[0][0], index_min_element[1][0]] = maximum
  
print("изммененная матрица\n",array)
