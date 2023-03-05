import numpy as np

array = np.random.randint(-5, 10, (15))

print(array)
print ('Количество нулей:', len(np.nonzero(array == 0)[0]))
print ('Количество положительных элементов:', len(np.nonzero(array > 0)[0]))
print ('Количество отрицательных элементов:', len(np.nonzero(array < 0)[0]))
   
