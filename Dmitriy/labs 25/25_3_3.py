import numpy as np

summ = 0

lst = np.random.randint(-50, 50, 15)
min = np.argmin(lst)
max = np.argmax(lst)
print(lst)
print("индекс максимального элемента:",max ,"\nииндекс минимального элемента:", min)

if max < min:
    answer = np.sum(lst[max:min + 1]) 
else:
    answer = np.sum(lst[min:max + 1])

print('Сумма:', answer)


