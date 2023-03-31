n =int(input('Матрица со стороной: '))
a = [[0]*n for i in range(n)]

for i in range(len(a)):
    for j in range(len(a[i])):
        if i == j:
            a[i][j] = 1
        elif i < j:
            a[i][j] = 0
        else:
            a[i][j] = 2
    print()

for i in a:
    print(' '.join([str(j) for j in i]))