import numpy as np

array = np.random.randint(-30, 15, (8, 5))

print(array)

maximum = np.max(array)
array = np.abs(array)

print("максимум:", maximum)
print('Элементов по модулю больше максимума', np.sum(array > maximum))
