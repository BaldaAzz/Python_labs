'''
import random

kol = 0
gr1 = int(input('Введите нижний предел: '))
gr2 = int(input('Введите верхний предел: '))
spisok = [random.randint(-50,100) for i in range(15)]

print(spisok)

for i in range(len(spisok)):
    if spisok[i] >= gr1 and spisok[i] <= gr2:
        kol += 1

print(kol)

'''

#если диапозон с калвиатуры
import random

kol = 0
gr1 = int(input('Введите нижний предел: '))
gr2 = int(input('Введите верхний предел: '))
PrMin = int(input('Введите мин диапозон: '))
PrMax = int(input('Введите макс диапозон: '))
spisok = [random.randint(PrMin,PrMax) for i in range(15)]

print(spisok)

for i in range(len(spisok)):
    if spisok[i] >= gr1 and spisok[i] <= gr2:
        kol += 1

print(kol)
