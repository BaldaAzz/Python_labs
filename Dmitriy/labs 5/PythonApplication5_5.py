import random

min = int(input('Введите минимальное значение диапозона: '))
max = int(input('Введите максимальное значение диапозона: '))
min_element = int(input('Введите минимальное значение: '))
max_element = int(input('Введите максимальное значение: '))
summa = 0
lst = [random.randint(min ,max) for i in range(20)]

print(lst)

for i in range(len(lst)):
    if (lst[i] >= min_element) and (lst[i] <= max_element):
        summa += 1

print(summa)

