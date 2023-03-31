a = [[i * j for j in range(6)] for i in range(5)]

for i in range(1, len(a)):
    for j in range(1, len(a[i])):
        a[i][j] = i * j
        print(a[i][j], end=' ')
    print()