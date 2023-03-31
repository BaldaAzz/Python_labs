lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

lst[lst.index(max(lst))], lst[lst.index(min(lst))] = lst[lst.index(min(lst))], lst[lst.index(max(lst))]

print(lst)
