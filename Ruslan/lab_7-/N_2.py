from random import randint


lst1 = [randint(0, 20) for i in range(10)]
print(lst1)

print([item for item in set(lst1) if lst1.count(item) > 1])
