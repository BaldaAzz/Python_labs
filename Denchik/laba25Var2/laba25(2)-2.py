"""2.	Дан двумерный массив размерностью 5х6.
Определите индекс максимального и минимального элемента, на место максимального поставьте минимальный и наоборот."""

import numpy as np

mass = np.random.randint(0, 10, (5, 6))

print(mass)

mass_max = np.argmax(mass.reshape(1, 30))
mass_min = np.argmin(mass.reshape(1, 30))
mass_max_index = [mass_max // mass.shape[0],mass_max % mass.shape[1]]
mass_min_index = [mass_min // mass.shape[0],mass_min % mass.shape[1]]

print(f'index max: {mass_max_index}')
print(f'index min: {mass_min_index}')

mass[mass_max_index[0]][mass_max_index[1]], mass[mass_min_index[0]][mass_min_index[1]] = mass[mass_min_index[0]][mass_min_index[1]], mass[mass_max_index[0]][mass_max_index[1]]

print(mass)
