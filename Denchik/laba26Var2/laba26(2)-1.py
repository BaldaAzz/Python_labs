"""Сгенерировать одномерный массив размерностью 20, заполнив его числами в диапазоне от -5 до 4.
Посчитать сколько среди них положительных, отрицательных и нулевых значений.
Вывести на экран элементы массива и посчитанные количества.
"""
import numpy as np

mass = np.array(np.random.randint(-5, 4, 20))
mass_pozit = np.extract( mass > 0, mass)
mass_negativ = np.extract( mass < 0, mass)
mass_zero = np.extract( mass == 0, mass)

print(mass)
print(mass_pozit.size,'положительных элементов :',mass_pozit)
print(mass_negativ.size,'отрицательных элементов :',mass_negativ)
print(mass_zero.size,'нулевых элементов :',mass_zero)
