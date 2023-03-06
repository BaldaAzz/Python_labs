"""
В созданном двумерном массиве размерностью 6х6 найти элементы, которые в нем
встречаются только один раз, и вывести их на экран.
"""

import numpy as np

mass = np.array(np.random.randint( 0, 12, 36)).reshape(6, 6)
mass_unique = np.unique(mass, return_counts = True,)

print(mass)
print(mass_unique)
print(np.extract( mass_unique[1] == 1, mass_unique[0]))
