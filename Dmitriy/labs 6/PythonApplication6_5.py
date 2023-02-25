n = int(input('Введите количетсво строк: '))
m = int(input('Введите количество столбцов: '))
matrix = []
lst1 = []

print('выведите построчно ваши элементы матрицы ')

for i in range(n):
    lst1.append(list(map(int,input().split())))

print('Перевернутая матрицa: ')

matrix = [[lst1[i][j] for i in range(len(lst1))] for j in range(len(lst1[i]))]

for j in range(m):
    for i in range(n-1,-1,-1):
        print(matrix[j][i], end = ' ')
    print()
    