"""
Сгенерировать одномерный массив размерностью 20, заполнив его числами в диапазоне от -5 до 4.
Посчитать сколько среди них положительных, отрицательных и нулевых значений.
Вывести на экран элементы массива и посчитанные количества.
"""
import numpy as np

mass = np.random.randint(-5, 4, 20)

print(mass)
print(poz_count := np.sum(mass > 0), 'положительных элементов :',
      poz_elenets := np.extract(mass > 0, mass))
print(neg_count := np.sum(mass < 0), 'отрицательных элементов :',
      neg_elenets := np.extract(mass < 0, mass))
print(zero_count := np.sum(mass == 0), 'нулевых элементов :',
      zero_elenets := np.extract(mass == 0, mass))
