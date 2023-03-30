import numpy as np

summ = 0

array = np.random.randint(-50, 50, 15)
minimum = np.argmin(array)
maximum = np.argmax(array)

print(array)
print("индекс максимального элемента:", maximum, "\nииндекс минимального элемента:", minimum)

if maximum < minimum:
    answer = np.sum(array[maximum:minimum + 1]) 
else:
    answer = np.sum(array[minimum:maximum + 1])

print('Сумма:', answer)


