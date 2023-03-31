n = 4
m = 4
matrix = []

for i in range(n):
    matrix.append([5] * m)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            matrix[i][j] = 1
        elif j <= i:
            matrix[i][j] = 2
        elif j >= i:
            matrix[i][j] = 0

for row in matrix:
    for item in row:
        print(item, end=' ')
    print()