"""2.	Дан двумерный массив размерностью 5х6.
Определите индекс максимального и минимального элемента, на место максимального поставьте минимальный и наоборот."""

import numpy as np 

mass = np.arange(5*6).reshape(5,6)

print(mass)
mass_max = np.argmax(mass)
mass_min = np.argmin(mass)

print('index max element(', mass_max%mass.shape[0],',',mass_max//mass.shape[0],')')
print('index min element(', mass_min%mass.shape[0],',',mass_min//mass.shape[0],')')
print(mass)
