import random

lst = [random.randint(1, 5) for i in range(10)]

print(lst)

lst_rep = set([i for i in set(lst) if lst.count(i) > 1])

print(lst_rep if lst_rep else 'Повторяющихся элементов нет')
