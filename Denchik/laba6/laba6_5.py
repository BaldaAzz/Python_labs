import random

n = int(input('Введите количетсво строк - '))
m = int(input('Введите количество столбцов - '))
s = [[random.randint(-10,30) for i in range(m)] for j in range(n)]
for i in range (n):

     for j in range(m):
        print(s[i][j], end=' ')
     print()

print('Перевернутая матрицa: ')

for i in range(n):
    for j in range(m):
        print(s[m-j-1][i], end=' ')
    print()