'''
2.	Дан двумерный массив размерностью 6х8. 
Определите индекс максимального и минимального элемента, 
на место максимального поставьте минимальный и наоборот.
'''

import numpy as np


matrix = np.random.randint(-10, 10, size=(6, 8))
print(matrix,'\n\n')

indexes_max_value = np.unravel_index(np.argmax(matrix), matrix.shape)
indexes_min_value = np.unravel_index(np.argmin(matrix), matrix.shape)

max_value = matrix[indexes_max_value[0], indexes_max_value[1]]
min_value = matrix[indexes_min_value[0], indexes_min_value[1]]


matrix[indexes_max_value[0], indexes_max_value[1]] = min_value
matrix[indexes_min_value[0], indexes_min_value[1]] = max_value

print(matrix)