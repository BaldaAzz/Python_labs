lst = [1, 2, 3, 4, 5, 4, 3, 2, 1]
lst_rewirse = lst[:: - 1]

if lst == lst_rewirse:
    print("Список является симметричным")
else:
    print("Список не является симметричным")