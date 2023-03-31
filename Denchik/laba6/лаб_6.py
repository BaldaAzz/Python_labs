# Задание 1
# Вывести двумерный числовой список на экран построчно, разделяя числа пробелами внутри одной строки
# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()


# Задание 2
# n = 4
# a = [[0]*n for i in range(n)]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if i == j:
#             a[i][j] = 1
#         elif i < j:
#             a[i][j] = 0
#         else:
#             a[i][j] = 2
#     print()
# for i in a:
#     print(' '.join([str(j) for j in i]))



# Задание 3
# Нужно задать числовой список. В этом списке n = 5 строк, m = 6 столбцов,
# и элемент в строке i и столбце j вычисляется по формуле: a[i][j] = i * j

# a = [[i * j for j in range(6)] for i in range(5)]
# for i in range(1, len(a)):
#     for j in range(1, len(a[i])):
#         print(a[i][j], end=' ')
#     print()



# Задание 4
# Найдите индексы первого вхождения максимального элемента массива.
# n = int(input('Введите количетсво строк - '))
# m = int(input('Введите количество столбцов - '))
# import random
# s = [[random.randint(-10,30) for j in range(m)] for i in range(n)]
# max_i = 0
# max_j = 0
# max = s[0][0]
# for i in range (len(s)):
#     for j in range(len(s[i])):
#         print(s[i][j], end=' ')
#         if s[i][j] > max:
#             max = s[i][j]
#             max_i = i
#             max_j = j
#     print()
# print(f'Максимальный элемент {max} с индексами: строка - {max_i} и столбец - {max_j}')



# Задание 5
# Дан прямоугольный массив размером n×m. Поверните его на 90 градусов
# по часовой стрелке, записав результат в новый массив размером m×n
n = int(input('Введите количетсво строк - '))  # type: ignore
m = int(input('Введите количество столбцов - '))
import random
# import numpy
# s = numpy.array([[random.randint(-10,30) for i in range(m)] for j in range(n)])
# for i in range (len(s)):
#     for j in range(len(s[i])):
#         print(s[i][j], end=' ')
#     print()
# print('Перевернутая матрицa: ')
# s1 = numpy.rot90(numpy.rot90(numpy.rot90(s)))
# for i in range(len(s1)):
#     for j in range(len(s1[i])):
#         print(s1[i][j], end=' ')
#     print()
s = [[random.randint(-10,30) for i in range(m)] for j in range(n)]
for i in range (n):
    for j in range(m):
        print(s[i][j], end=' ')
    print()
print('Перевернутая матрицa: ')
# print(s)
for i in range(n):
    for j in range(m):
        print(s[n-i-1][j], end=' ')
    print()
