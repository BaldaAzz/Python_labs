import numpy as np

summ = 0

lst = np.random.randint(-50,50,15)
min = np.argmin(lst)
max = np.argmax(lst)
print(lst)
print("индекс максимального элемента:",max ,"\nииндекс минимального элемента:", min)

if max < min:
    answer = np.sum(lst[max:min]) 
    answer -= np.max(lst)
else:
    answer = np.sum(lst[min:max])
    answer -= np.min(lst)
print('Сумма:', answer)


