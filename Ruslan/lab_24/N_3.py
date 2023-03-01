'''
3.	Задан одномерный массив размерностью 9. 
Переформатировать в двумерный массив. 
Элементы главной диагонали заменить на 1.
'''

import numpy as np


mass = np.array(np.arange(9))
print(mass)

matrix = mass.reshape(3, 3)
print(matrix)


np.fill_diagonal(matrix, 1)
print(matrix)
