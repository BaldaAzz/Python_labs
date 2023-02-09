from random import randint


lst = [randint(1,3) for i in range(5)]

print(lst)

unique = [i for i in set(lst) if lst.count(i) > 1]

if len(unique) == 0:
    print("Повторяющихся элементов нет")

else:
    print(unique)