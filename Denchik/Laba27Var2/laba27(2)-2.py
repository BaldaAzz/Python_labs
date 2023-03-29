from numpy import log, array
import pandas as pd

# Создайте новый объект Series из массива NumPy, состоящий из элементов -9 4 10 14 25 3 5 11.
mass = array([-9, 4, 10, 14, 25, 3, 5, 11])
s = pd.Series(mass)

print(s,'\n')

# Выведите значения от 5 до 15.

print(s[5 < s][s < 15],'\n')

# Нечетным индексам исходного объекта Series прибавьте число 6.

s[s.index % 2 != 0] += 6

print(s, '\n')
 
# Найдите логарифм из значений измененного массива.

s_log = log(s)

print(s_log,'\n')
