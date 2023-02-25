lst = [[8, 2, 3, 2], [3, 2, 1, 0], [2, 3, 1, 4], [5, 3, 2, 1]]

for i in range(len(lst)):
    for j in range(0, i):
        lst[i][j] = 2
    lst[i][i] = 1
    for j in range(i + 1, len(lst)):
        lst[i][j] = 0

for n in lst:
    print(' '.join([str(element) for element in n]))



