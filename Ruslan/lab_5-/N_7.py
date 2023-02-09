from random import randint

lst = []
lst_len = 15

for i in range(lst_len):
    lst.append(randint(-25, 25)) 

print(lst)

min_element = lst[0]
index_min = 0
max_element = lst[0]
index_max = 0

for i in range(len(lst)):
    if min_element > lst[i]:
        min_element = lst[i]
        index_min = i
    if max_element < lst[i]:
        max_element = lst[i]
        index_max = i

lst.insert(index_min, max_element)
lst.pop(index_min + 1)
lst.insert(index_max, min_element)
lst.pop(index_max + 1)

print(lst)
