'''1.	Даны два двумерных массива. 
Посчитайте сумму массивов, произведение транспонированных матриц. 
Посчитайте сумму двух матриц и определите, какая сумма больше.'''

import numpy as np


matrix_A = np.random.randint(0, 10, size=(3, 3))
matrix_B = np.random.randint(0, 10, size=(3, 3))

print(matrix_A)
print()
print(matrix_B)
print('\n\n')

sum_matrix = matrix_A + matrix_B
print('Сумма матриц')
print(sum_matrix)
print()

prod_transposed_matrices = matrix_A.T * matrix_B.T
print('Произведение транспонированых матриц')
print(prod_transposed_matrices)

sum_matrix_A = np.sum(matrix_A)
sum_matrix_B = np.sum(matrix_B)

if sum_matrix_A > sum_matrix_B:
    print(f'Сумма матрицы A ({sum_matrix_A}) > сумма матрицы B({sum_matrix_B})')
else:
    print(f'Сумма матрицы B ({sum_matrix_B}) > сумма  матрицы A ({sum_matrix_A})')