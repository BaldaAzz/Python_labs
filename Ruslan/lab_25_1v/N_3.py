'''
3.	В одномерном массиве найти сумму элементов, 
находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.
'''

import numpy as np


mass = np.random.randint(0, 10, 10)
print(mass)

summa = 0
if np.argmin(mass) < np.argmax(mass):
    summa = np.sum(mass[np.argmin(mass) + 1: np.argmax(mass)])
else:
    summa = np.sum(mass[np.argmax(mass) + 1: np.argmin(mass)])

print(summa)