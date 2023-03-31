n, m = map(int, input().split())
matrix = []
max_row, max_col = 0, 0

for i in range(n):
    matrix.append(list(map(int,input().split())))

max_elem = matrix[0][0]

for i in range(len(matrix) - 1):
    for j in range(len(matrix[i]) - 1):
        if max_elem < matrix[i][j]:
            max_row = i
            max_col = j
            max_elem = matrix[i][j]

print(max_row, max_col)


# 3 4
# 0 3 2 4
# 2 3 5 5
# 5 1 2 3
