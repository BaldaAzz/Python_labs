'''
1. Задана двумерная матрица отрицательных чисел.
Посчитать сумму элементов в каждом столбце.
Определить, какой столбец содержит минимальную сумму.
'''

import numpy as np

mass = np.array(np.random.randint(-20, -1, 25)).reshape(5, 5)

print(mass)

mass_sum = mass.sum(axis=0)
min_column = np.argmin(mass_sum)

print('Sum of colums:', mass_sum)
print('Column index with min sum:', min_column, '\nMin sum :', min(mass_sum))
