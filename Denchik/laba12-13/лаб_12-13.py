# Задание №1.
# class Workers:
#     n = 0
#     with open('lab12.txt', 'w', encoding='utf-8') as f:
#         while n != 2:
#             salary = input('Введите зарплату: ')
#             bonus = input('Введите премию: ')
#             last_name = input('Введите фамилию: ')
#             f.write(f'{salary} {bonus} {last_name}\n')
#             n = int(input('Хотите ввести данные (1 - да, 2 - нет)? '))
#
#     def __init__(self):
#         pass
#
#     def get_general_salary(self):
#         with open('lab12.txt', 'r', encoding='utf-8') as file:
#             s = file.read()
#         s = s.split()
#         summa_salary = sum([int(s[i]) for i in range(0, len(s), 3)])
#         summa_bonus = sum([int(s[i]) for i in range(1, len(s), 3)])
#         all_salary = (summa_salary+summa_bonus)/0.7
#         print(round(all_salary))
#
# worker = Workers()
# worker.get_general_salary()




# Задание №2.
# import random
# class Massive:
#     def __init__(self, n, a, b):
#         self.n = n
#         self.a = a
#         self.b = b
#
#     def vyvod(self):
#         lst = [random.randint(self.a, self.b) for i in range(self.n)]
#         for i in range(len(lst)):
#             print(lst[i], end=' ')
#
# n = int(input('Введите размерность массива: '))
# a = int(input('Введите нижнюю границу диапазона: '))
# b = int(input('Введите верхнюю границу диапазона: '))
# mass = Massive(n, a, b)
# mass.vyvod()