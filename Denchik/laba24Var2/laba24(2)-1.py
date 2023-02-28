# 1. Задана двумерная матрица отрицательных чисел.
# Посчитать сумму элементов в каждом столбце.
# Определить, какой столбец содержит минимальную сумму.

from random import randint
import numpy as np

lst = []
lst.append([randint(-20, -1) for i in range(25)])
mass = np.array(lst).reshape(5, 5)
print(mass)
mincol_index = 0
mass_sum = mass.sum(axis=1)
for i in range(0,len(mass)-1,1):
    print(mass_sum[i],'>',mass_sum[i+1] )
    print(i)
    if mass_sum[i+1] < mass_sum[i]:
        b = mass_sum[i+1]
        mincol_index = i+1
print('Sum of colums', mass_sum)
print('column with min sum', mincol_index, '\n min sum =', b)
