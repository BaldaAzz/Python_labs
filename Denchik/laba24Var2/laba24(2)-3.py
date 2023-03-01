# Задан одномерный массив размерностью 10. 
# Переформатировать в двумерныймассив.
# Элементы главной диагонали заменить на 0.

import numpy as np

mass = np.arange(10)
mass = mass.reshape(2,5)

print(mass)

for i in range(len(mass)):
    for j in range(len(mass[0])):
        if i == j:
            mass[i][j] = 0

print(mass)
