'''1.	Даны два двумерных массива. 
Посчитайте сумму массивов, произведение транспонированных матриц. 
Посчитайте сумму двух матриц и определите, какая сумма больше.'''

import numpy as np


len_array = 9

matrix_A = np.array([np.random.randint(0, 10) for i in range(len_array)]).reshape(3, 3)
matrix_B = np.array([np.random.randint(0, 10) for i in range(len_array)]).reshape(3, 3)

print(matrix_A)
print()
print(matrix_B)
print('\n\n')
print('Сумма матриц')
print(matrix_A + matrix_B)
print()
print('Произведение транспонированых матриц')
print()

sum_matrix_A = np.sum(matrix_A)
sum_matrix_B = np.sum(matrix_B)

if sum_matrix_A > sum_matrix_B:
    print(f'Сумма матрицы A ({sum_matrix_A}) > сумма матрицы B({sum_matrix_B})')
else:
    print(f'Сумма матрицы B ({sum_matrix_B}) > сумма  матрицы A ({sum_matrix_A})')