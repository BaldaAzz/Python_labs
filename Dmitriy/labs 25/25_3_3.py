import numpy as np

summ = 0

array = np.random.randint(-50, 50, 15)
min = np.argmin(array)
max = np.argmax(array)

print(array)
print("индекс максимального элемента:",max ,"\nииндекс минимального элемента:", min)

if max < min:
    answer = np.sum(array[max:min + 1]) 
else:
    answer = np.sum(array[min:max + 1])

print('Сумма:', answer)


