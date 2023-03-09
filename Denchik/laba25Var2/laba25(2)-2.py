"""
2.	Дан двумерный массив размерностью 5х6.
Определите индекс максимального и минимального элемента, на место максимального поставьте минимальный и наоборот.
"""

import numpy as np

mass = np.random.randint(0, 10, (5, 6))

print(mass)

mass_max = np.max(mass)
mass_min = np.min(mass)
max_ind = np.where(mass == mass_max)
min_ind = np.where(mass == mass_min)

print(f'index max row: {max_ind[0]}\nindex max col: {max_ind[1]}')
print(f'index min row: {min_ind[0]}\nindex min col: {min_ind[1]}')

mass[max_ind[0][0], max_ind[1][0]] = mass_min
mass[min_ind[0][0], min_ind[1][0]] = mass_max

print(mass)
