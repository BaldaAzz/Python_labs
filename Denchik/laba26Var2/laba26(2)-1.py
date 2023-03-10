"""
Сгенерировать одномерный массив размерностью 20, заполнив его числами в диапазоне от -5 до 4.
Посчитать сколько среди них положительных, отрицательных и нулевых значений.
Вывести на экран элементы массива и посчитанные количества.
"""
import numpy as np

mass = np.random.randint(-5, 4, 20)

mass_more_0 = np.sum(mass > 0)
mass_less_0 = np.sum(mass < 0)
mass_eq_0 = np.sum(mass == 0)
el_mass_more_0 = np.extract(mass > 0, mass)
el_mass_less_0 = np.extract(mass < 0, mass)
el_mass_eq_0 = np.extract(mass == 0, mass)

print(mass)
print(mass_more_0, 'положительных элементов :',el_mass_more_0)
print(mass_less_0, 'отрицательных элементов :',el_mass_less_0)
print(mass_eq_0, 'нулевых элементов :',el_mass_eq_0)
