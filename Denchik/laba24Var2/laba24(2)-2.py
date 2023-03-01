# Задана матрица 4х8. Возвести элементы матрицы в куб.

from random import randint
import numpy as np

lst = []
lst.append([randint(-10, 10) for i in range(32)])
mass = np.array(lst).reshape(4, 8)

print(mass)

mass **= 3

print(mass)
