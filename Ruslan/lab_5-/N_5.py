from random import randint


lst = []
LIST_LEN = 20
list_random = [randint(-100, 100) for i in range(LIST_LEN)]

num_min = int(input('Введите минимальное число диапазона: '))
num_max = int(input('Введите максимальное число диапазона: '))

for num in list_random:
    if num_min <= num <= num_max:
        lst.append(num)

print(list_random)
print(lst)

