"""
В созданном двумерном массиве размерностью 6х6 найти элементы, которые в нем
встречаются только один раз, и вывести их на экран.
"""

import numpy as np

mass = np.random.randint(0, 12, (6, 6))
mass_unique_and_counts = np.unique(mass, return_counts=True)
mass_unique_elements = mass_unique_and_counts[0]
mass_unique_counts = mass_unique_and_counts[1]
mass_unique_count_eq_1 = mass_unique_elements[mass_unique_counts == 1]

print('Massiv\n', mass)
print('Unique elements in massiv\n', mass_unique_elements)
print('The number of each uniqie element in massiv\n', mass_unique_counts)
print('Elements that meet once\n', mass_unique_count_eq_1)

# время выполнение кода 0.00016
