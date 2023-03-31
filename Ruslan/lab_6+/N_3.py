n = 5
m = 6
matrix = []

for i in range(n):
    matrix.append([0] * m)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = i * j


for row in matrix:
    for item in row:
        print(item, end=' ')
    print()
