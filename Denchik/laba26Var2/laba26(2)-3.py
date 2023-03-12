"""
Создать двумерный массив размерностью 6х7 в диапазоне значений от -15 до 14 включительно.
Определить количество элементов по модулю больших, чем максимальный.
"""

import numpy as np

mass = np.random.randint(-15, 15, (6, 7))
mass_max = np.max(mass)
mass_abs = abs(mass)
elements_modular_large = np.extract(mass_abs > mass_max, mass)
elements_modular_large_value = elements_modular_large.size

print(mass)
print('Max element:', mass_max)
print('Number of element(s) modular large than max:', elements_modular_large_value)
print('Max element(s) modulo:', elements_modular_large)
