# Задана матрица 4х8. Возвести элементы матрицы в куб.

from random import randint
import numpy as np

mass = np.array(np.random.randint(-10, 10, 32)).reshape(4, 8)

print(mass)

mass **= 3

print(mass)
