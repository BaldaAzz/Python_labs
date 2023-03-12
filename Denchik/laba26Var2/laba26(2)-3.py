"""
Создать двумерный массив размерностью 6х7 в диапазоне значений от -15 до 14 включительно.
Определить количество элементов по модулю больших, чем максимальный.
"""

import numpy as np

mass = np.random.randint(-15, 15, (6, 7))
elements_modular_large = np.extract(abs(mass) > np.max(mass), mass)
elements_modular_large_value = elements_modular_large.size

print(mass)
print('Max element:', max_element := np.max(mass))
print('Number of element(s) modular large than max:', elements_modular_large_value)
print('Max element(s) modulo:', elements_modular_large)
