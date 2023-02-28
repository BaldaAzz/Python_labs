import numpy as np
from random import randint


matrix = []
for i in range(5):
    matrix.append([np.random.randint(0, 9) for j in range(5)])

matrix_np = np.array(matrix, dtype=int)
print(matrix_np) 

sums = matrix_np.sum(axis=0)

print('\n',sums)
print(sums.tolist().index(max(sums)))
