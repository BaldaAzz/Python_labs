ErrorMessage = {}
flag = True
while flag:
    ErrorMessage.clear()

    hashtegs = input('\nВведите текст: ')
    hashtegs = hashtegs.lower()
    hashteg = hashtegs.split()
    unequi_hashtegs = set(hashteg)

    if hashteg:
        
        for i in range(len(hashteg)):
            if hashteg[i][0] != '#':
                ErrorMessage.update(heshteg =  'Тег должен начинаться с # ')

            if len(hashteg[i]) > 20:
                ErrorMessage.update( long = 'Длина тега превышает 20 символов')

            if hashteg[i][0] == '#' and len(hashteg[i]) == 1:
                ErrorMessage.update(one_hesh =  'Хэш-тег состоит из одного символа #')

            if hashteg[i].count('#') >= 2:
                ErrorMessage.update(no_probel = 'Между хэш-тегами отсутствует пробел')

        if len(hashteg) > len(unequi_hashtegs):
            ErrorMessage.update(repeat = 'Повторение хеш-тегов')

        if len(hashteg) > 5:
            ErrorMessage.update(so_much_hesh = 'Количество тегов превышает 5')

        if len(ErrorMessage) == 0:
            print('Succes')
            flag = False

        for value in ErrorMessage.values():
            print(value)
    else:
        print('Succes')
        flag = False