"""
В созданном двумерном массиве размерностью 6х6 найти элементы, которые в нем
встречаются только один раз, и вывести их на экран.
"""

import numpy as np

mass = np.array(np.random.randint(0, 10, 36)).reshape(6, 6)

mass_unique = np.unique(mass, return_index=False, return_inverse=False, return_counts=False, axis=None)

print(mass)
print(mass_unique)
