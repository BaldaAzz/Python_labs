import random

s = [random.randint(-100,100) for i in range(15)]

print(s)

summa = 0
kol = 0

for i in range(len(s)):
    if s[i] < 0:
        summa += s[i]
        kol += 1
        
sred =int(summa / kol)
min_index = s.index(min(s))
s.insert(min_index, sred)

print('Среднее арифметическое чисел равно ', sred, '\nМинимальный элемент списка ', min(s),
      '\n', s)