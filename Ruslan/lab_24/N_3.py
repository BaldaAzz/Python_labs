import numpy as np


matrix = np.array(np.arange(0, 9), dtype=int).reshape(3,3)
print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            matrix[i, j] = 1

print(matrix)