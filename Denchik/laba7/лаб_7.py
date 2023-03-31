# Задание 1
# import random
# tuple_1 = tuple([random.randint(0, 5) for i in range(10)])
# tuple_2 = tuple([random.randint(-5, 0) for i in range(10)])
# tuple_3 = tuple_1 + tuple_2
# print(tuple_3, f'\nКоличество нулей: {tuple_3.count(0)}')


# Задание 2
# import random
# sp = [random.randint(1,5) for i in range(10)]
# print(sp)
# set_sp = set([i for i in set(sp) if sp.count(i)>1])
# print(set_sp if set_sp else 'Повторяющихся элементов нет')


# Задание 3
# print(len(set(set(input(': ').split()) & set(input(': ').split()))))
import random
print(len(set([random.randint(1,10) for i in range(10)]) & set([random.randint(1,20) for i in range(10)])))


# Задание 4
# import random
# print(sorted(set([random.randint(1,20) for i in range(10)]) & set([random.randint(1,20) for i in range(10)])))


# Задание 5
# sp = input('Введите числа:').split()
# for i in range(len(sp)):
#     print('YES' if sp[i] in sp[:i] else 'NO' , sep='\n')
