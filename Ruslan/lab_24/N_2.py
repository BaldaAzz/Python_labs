'''
2.	Задана матрица 3х5. 
Возвести элементы матрицы в квадрат.
'''

import numpy as np


matrix = np.array(np.arange(15)).reshape(3, 5)
print(matrix) 

matrix **= 2

print(matrix)