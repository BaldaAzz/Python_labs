import numpy as np


matrix = []
for i in range(3):
    matrix.append([np.random.randint(0, 9) for j in range(5)])

matrix_np = np.array(matrix, dtype=int)
print(matrix_np) 

matrix_np **= 2

print(matrix_np)