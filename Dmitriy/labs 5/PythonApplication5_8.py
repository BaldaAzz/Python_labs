from random import randint

lst = [randint(1,10) for i in range(10)]
lst2 = list()

print(lst)

for i in set(lst):
    if lst.count(i) > 1:
       lst2.append(i)

print(lst2)


