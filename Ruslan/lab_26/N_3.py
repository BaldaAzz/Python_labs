'''
3.	Создать одномерный массив из 20 элементов в диапазоне значений от -10 до 10 включительно. Определить количество элементов по модулю больших, чем максимальный.
'''

import numpy as np


mass = np.random.randint(-10, 11, 20)
print(mass)

max_value = mass[np.argmax(mass)]
print(max_value)

numbers_greater_than_max_element = np.extract(max_value < abs(mass), mass)
counter_greatest_values = np.size(numbers_greater_than_max_element)
print(counter_greatest_values)