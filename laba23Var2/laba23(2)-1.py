# 1. Создайте одномерный массив размерностью 9. Замените третий элемент на 0.
# Поверьте, присутствуют ли в массиве элементы со значением 2. Переформатируйте одномерный
# массив в двумерный и определите количество столбцов и строк.

import numpy as np

mass = np.arange(9)
print(mass)
print(len(mass),'len')
mass[3] = 0
print(' 2 in massiv ',2 in mass)
mass = mass.reshape(3,3)
print(mass.shape, 'shape')
print(mass)
