# 2. Создайте двумерный массив вещественных чисел размерностью 9х5.
# Массив содержит отрицательные и положительные элементы.
# Выведите последнюю строку массива.
# Замените в первой строке элементы числом 1. Определите длину двумерного массива.

import numpy as np
from random import randint

lst = []
lst.append([randint(-10,10) for i in range(45)])
mass = np.array(lst).reshape(9,5)
print(mass[-1] ,'последняя строка')
mass[0] = 1
print(mass)
print(mass.size)