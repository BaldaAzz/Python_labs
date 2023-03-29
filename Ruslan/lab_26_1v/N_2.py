'''
2.	В созданном двумерном массиве размерностью 7х5 найти элементы, 
которые в нем встречаются только один раз, и вывести их на экран.
'''

import numpy as np


matrix = np.random.randint(-15, 15, size=(7, 5))
print(matrix)

mass_unique = np.unique(matrix, return_counts=True)
print(np.extract(mass_unique[1] == 1, mass_unique[0]))
