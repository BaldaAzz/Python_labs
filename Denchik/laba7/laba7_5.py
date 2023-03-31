sp = input('Введите числа:').split()

for i in range(len(sp)):
    print('YES' if sp[i] in sp[:i] else 'NO', sep='\n')
