""" 
3.	В одномерном массиве найти произведение элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в произведение не включать.
"""

import numpy as np

mass = np.random.randint(0, 10, 10)

print(mass)

if np.argmin(mass) < np.argmax(mass):
    print(np.prod(mass[np.argmin(mass) + 1: np.argmax(mass)]))
else:
    print(np.prod(mass[np.argmax(mass) + 1: np.argmin(mass)]))
