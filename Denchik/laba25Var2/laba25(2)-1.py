# 1. Даны два двумерных массива.
#  Посчитайте сумму транспонированных матриц,произведение матриц.
#  Определите, какая сумма больше.

from random import randint
import numpy as np

lst = []
lst.append([randint(-10, 10) for i in range(25)])
mass_1 = np.array(lst).reshape(5, 5)

lst = []
lst.append([randint(-10, 10) for i in range(25)])
mass_2 = np.array(lst).reshape(5, 5)

mass_sum = (mass_1 + mass_2).T
mass_multi = mass_1 * mass_2
mass_1_sum = sum(mass_1)
mass_2_sum = sum(mass_2)
mass_sim = mass_1_sum > mass_2_sum


print(mass_1)
print(mass_2)
print(mass_sum)
print(mass_multi)
print(mass_sim)
