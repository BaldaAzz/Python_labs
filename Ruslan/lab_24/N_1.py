'''
1.	Задана  двумерная матрица положительных чисел. 
Посчитать сумму элементов в каждом столбце. 
Определить, какой столбец содержит максимальную сумму.
'''

import numpy as np


matrix = np.random.randint(0, 9, size=(3, 3))

print(matrix) 

sums = matrix.sum(axis=0)

print('\n',sums)
print(f'Столбец {np.argmax(sums)} имеет максимальную сумму')
