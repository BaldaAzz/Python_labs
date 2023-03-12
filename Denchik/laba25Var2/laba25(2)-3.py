""" 
3.	В одномерном массиве найти произведение элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в произведение не включать.
"""

import numpy as np

mass = np.random.randint(0, 10, 10)

print(mass)

mass_min = np.argmin(mass)
mass_max = np.argmax(mass)

#подсчет произведения в приоритете от минимального до максимального
if mass_min < mass_max:
    sum_near = np.prod(mass[mass_min + 1: mass_max])
else:
    sum_near = np.prod(mass[mass_max + 1: mass_min])
    
print(f'Произведение между макс и мин элементом:\n{sum_near}')
