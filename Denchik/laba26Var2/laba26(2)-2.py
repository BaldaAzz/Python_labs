"""
В созданном двумерном массиве размерностью 6х6 найти элементы, которые в нем
встречаются только один раз, и вывести их на экран.
"""

import numpy as np

mass = np.random.randint(0, 12, (6, 6))
mass_unique = np.unique(mass, return_counts=True)

print('Massiv\n', mass)
print('Unique elements in massiv\n', mass_unique[0])
print('The number of each uniqie element in massiv\n', mass_unique[1])
print('Elements that meet once\n', mass_unique[0][mass_unique[1] == 1])

# время выполнение кода 0.00016
