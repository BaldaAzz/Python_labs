'''1.	Создайте одномерный массив размерностью 6.  
Замените первый элемент на противоположный.  
Поверьте, присутствуют ли в массиве элементы со значением 5. 
Переформатируйте одномерный массив в двумерный и определите количество столбцов и строк.  '''

import numpy as np


mass = np.random.randint(-10, 10, 6)
print(mass)

mass[0] = -mass[0]
print(mass)

print(5 in mass)

print(mass.reshape(2, 3))