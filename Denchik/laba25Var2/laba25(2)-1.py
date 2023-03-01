# 1. Даны два двумерных массива.
#  Посчитайте сумму транспонированных матриц,произведение матриц.
#  Определите, какая сумма больше.

from random import randint
import numpy as np

mass_1 = np.array(np.random.randint(-10, 10, 25)).reshape(5, 5)
mass_2 = np.array(np.random.randint(-10, 10, 25)).reshape(5, 5)

mass_sum = (mass_1 + mass_2).T
mass_multi = mass_1 * mass_2
mass_sim = 'сумма первого больше' if sum(sum(mass_1)) > sum(sum(mass_2)) else 'сумма второго больше'


print(mass_1)
print(mass_2)
print(mass_sum)
print(mass_multi)
print(mass_sim)
