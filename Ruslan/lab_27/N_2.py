'''
2. Создайте новый объект Series из массива NumPy, состоящий из элементов   
2  5  12  9 14 19  45 22. Выведите значения от 10 до 20. 
Четным значениям исходного объекта Series  прибавьте число 3. 
Найдите корень квадратный из значений измененного массива.
'''

import pandas as pd
import numpy as np


mass = np.array([2, 5, 12, 9, 14, 19, 45, 22])

ser = pd.Series(mass)

a = ser[np.logical_and(10 < ser, ser < 20)]
print(a)

a[a % 2 == 0] += 3
print(a)

sqrt_mass = a ** 0.5
print(sqrt_mass)