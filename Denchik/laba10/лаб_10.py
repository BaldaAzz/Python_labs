# Задание 1
# Во входном файле записаны 10 целых чисел, каждое в отдельной строке.
# Считать из текстового файла числа и записать их в другой текстовый файл в отсортированном виде.
# with open('ex_1.txt', 'r') as f:
#     s = f.read()
#     s = s.replace('\n', ' ')
# s = s.split()
# print(s)
# a = []
# for i in s:
#     if i.isdigit():
#         a.append(int(i))
##a.sort()
# print(a)
# with open('example1.txt', 'w') as file:
#     for i in range(len(a)):
#         file.writelines(f'{a[i]}\n')




# Задание 2
# В файле записаны в строку через пробел целые числа.
# Найти максимальное и минимальное число и записать в другой файл.
# with open('ex_2.txt', 'r') as f:
#     s = f.read()
# s = s.split()
# print(s)
# a = []
# for i in s:
#     if i.isdigit():
#         a.append(int(i))
# a_min = min(a)
# a_max = max(a)
# print(a_max, a_min)
# with open('example2.txt', 'w') as file:
#     file.write(f'Max:  {a_max} \nMin: {a_min}')


# Задание 3
# Считать из файла input.txt 10 чисел (числа записаны через пробел).
# Затем записать их произведение в файл output.txt.
# with open('input.txt', 'r') as f:
#     s = f.read()
# s = s.split()
# print(s)
# a = []
# for i in s:
#     if i.isdigit():
#         a.append(int(i))
# print(a)
# proizv = 1
# for i in range(len(a)):
#     proizv *= a[i]
# print(proizv)
# with open('output.txt', 'w', encoding='utf-8' ) as file:
#     file.writelines(f'Произведение: {proizv}')


# Задание 4
# Написать программу, которая считает количество строк,
# слов и букв в переданном ей файле.
# with open('ex_4.txt', 'r') as f:
#     s = f.read()
# line = s.count('\n') + 1
# word = s.count(' ') + line
# s = s.replace('\n', ' ')
# s = s.replace('.', ' ')
# s = s.replace(' ', '')
# letter = len(s)
# print(f'Input file contains: \n{letter} letters \n{word} words'
#       f' \n{line} lines ')



# Задание 5
# В файл записаны сведения о сотрудниках некоторой фирмы в виде:
# Иванов 45 бухгалтер
# Необходимо записать в текстовый файл сведения о сотрудниках,
# возраст которых меньше 40.
# with open('ex_5.txt', 'r', encoding='utf-8') as f:
#     s = f.readlines()
# print(s)
# a = []
# for i in range(len(s)):
#     s_1 = s[i].split()
#     a.append(s_1)
# print(a)
# with open('example5.txt', 'w', encoding='utf-8') as file:
#     for i in range(len(a)):
#         if int(a[i][1])<40:
#             file.writelines(f"{' '.join(a[i])}\n")




# Задание 6
# Дан файл с расписанием занятий на неделю. Помимо названия
# предмета в нем также указано лекция это, практическое занятие,
# или лабораторная работа. В одной строке может быть указан
# только один предмет с информацией о нем. Посчитать, сколько
# за неделю проходит практических занятий, лекций и лабораторных
# работ отдельно по каждому предмету.
# with open('ex_6.txt', 'r', encoding='utf-8') as f:
#     s = f.read()
# s = s.split()
# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)
# with open('example6.txt', 'w', encoding='utf-8') as file:
#     file.writelines(f"Лекций: {d.get('(лекц.)')}\n")
#     file.writelines(f"Практических: {d.get('(практ.)')}")
