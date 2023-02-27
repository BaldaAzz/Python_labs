import numpy as np 


# matrix = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])


T_matrix = matrix.T

print(T_matrix)

sums = {}
column = 0
for i in T_matrix:
    sums[column] = sum(i)
    column += 1

print(sums)

