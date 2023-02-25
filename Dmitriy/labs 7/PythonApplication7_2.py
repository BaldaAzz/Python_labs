from random import randint
lst = [randint(1,20) for i in range(10)]
set_lst = set(lst)
print(lst)
print(set_lst)

for i in set_lst:
    if lst.count(i) > 1:
        print(i)

