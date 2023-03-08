'''
3.	В одномерном массиве найти сумму элементов, 
находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.
'''

import numpy as np


mass = np.array(np.random.randint(0, 10, 10))
print(mass)

if np.argmin(mass) < np.argmax(mass):
    print(np.sum(mass[np.argmin(mass) + 1  : np.argmax(mass)])) 
else:
    print(np.sum(mass[np.argmax(mass) + 1  : np.argmin(mass)]))