import numpy as np

array = np.random.randint(-30, 15, (8, 5))

print(array)

max = np.max(array)
print("максимум:",max)

array = np.abs(array)

print('Элементов по модулю больше максимума', np.sum(array > max))
