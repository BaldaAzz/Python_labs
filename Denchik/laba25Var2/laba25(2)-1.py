"""1. Даны два двумерных массива.
 Посчитайте сумму транспонированных матриц,произведение матриц.
 Определите, какая сумма больше."""

import numpy as np

mass_1 = np.array(np.random.randint(-10, 10, 25)).reshape(5, 5)
mass_2 = np.array(np.random.randint(-10, 10, 25)).reshape(5, 5)

mass_sum = (mass_1 + mass_2).T #Транспориванная матрица сумм первой и второй матрицы
mass_multi = mass_1 * mass_2   #Матрица произведния первой и второй матрицы 
mass_sum_isbiggest = 'больше сумма первого' if np.sum(mass_1) > np.sum(mass_2) else 'больше сумма второго'



print('Первый масив \n',mass_1)
print('Второй масив \n',mass_2)
print('Сумма \n',mass_sum)
print('Произведение \n',mass_multi)
print(mass_sum_isbiggest)
