raw = input('Введите последовательность чисел через пробел: ')
individual = set()

for i in raw.split(' '):
    if i in individual:    
        print(i,'YES')
    else:
        print(i,'NO')
        individual.add(i)