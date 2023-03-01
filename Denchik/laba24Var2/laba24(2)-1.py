# 1. Задана двумерная матрица отрицательных чисел.
# Посчитать сумму элементов в каждом столбце.
# Определить, какой столбец содержит минимальную сумму.

from operator import index
from random import randint
import numpy as np

lst = []
lst.append([randint(-20, -1) for i in range(25)])
mass = np.array(lst).reshape(5, 5)

print(mass)

mass_sum = mass.sum(axis=0)

print('Sum of colums:', mass_sum)
print('column with min sum:',mass_sum.tolist().index(min(mass_sum)), '\nmin sum :', min(mass_sum))
