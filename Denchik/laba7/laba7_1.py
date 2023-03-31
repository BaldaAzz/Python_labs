import random

tuple_1 = tuple([random.randint(0, 5) for i in range(10)])
tuple_2 = tuple([random.randint(-5, 0) for i in range(10)])

tuple_3 = tuple_1 + tuple_2

print(tuple_3, f'\nКоличество нулей: {tuple_3.count(0)}')
