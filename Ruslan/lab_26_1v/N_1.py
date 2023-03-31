'''
1.	Сгенерировать двумерный массив размерностью 5х8, 
заполнив его числами в диапазоне от -5 до 4. 
Посчитать сколько среди них положительных, 
отрицательных и нулевых значений. 
Вывести на экран элементы массива и посчитанные количества.
'''

import numpy as np


matrix = np.random.randint(-5, 5, size=(5, 8))
print(matrix)

count_positiv_nums = np.size(matrix[matrix > 0])
count_negative_nums = np.size(matrix[matrix < 0])
count_zeros = np.size(matrix[matrix == 0])

print(f'Количество положительных чисел: {count_positiv_nums}')
print(f'Количество отрицательных чисел: {count_negative_nums}')
print(f'Количество нулевых значений: {count_zeros}')


