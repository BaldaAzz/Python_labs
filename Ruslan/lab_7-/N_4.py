from random import randint


lst1 = [randint(0, 15) for i in range(10)]
lst2 = [randint(0, 15) for i in range(10)]
print(lst1)
print()
print(lst2)
print()


print([i for i in sorted(set(lst1).intersection(lst2))]) 