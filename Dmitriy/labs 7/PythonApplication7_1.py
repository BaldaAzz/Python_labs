import random
cor1 = tuple([random.randint(0, 5) for i in range(10)])
cor2 = tuple([random.randint(-5, 0) for i in range(10)])
cor3 = cor1 + cor2
print("сумма кортежей",cor3,'количесвто нулей ',cor3.count(0))


