# Задание 1
# n = input('Введите текст: ').split()
# dictionary = {}
# for word in n:
#     if dictionary.get(word, 0):
#         dictionary[word] += 1
#     else:
#         dictionary[word] = 1
# m = max(dictionary.values())
# dict_sorted = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
# print(list(dict_sorted.keys())[0])




# Задание 2
# n = input('Введите текст: ')
# n = n.split()
# dictionary = {}
# for word in n:
#     if dictionary.get(word, 0):
#         dictionary[word] += 1
#     else:
#         dictionary[word] = 1
#
# dict_sorted = dict(sorted(dictionary.items(), key=lambda x: x[0]))
# for i in dict(sorted(dict_sorted.items(), key=lambda x: x[1], reverse=True)):
#     print(i)
    # hi hi what is your name my name is bond james bond my name is damme van damme claude van damme jean claude van damme



# Задание 3
# ErrorMessage = {}
# flag = True
# while flag:
#     ErrorMessage.clear()
#
#     s = input('\nВведите текст: ')  #read #books #hello #world #toy
#     s = s.lower()
#     s = s.split()
#     set1 = set(s)
#
#     if s:
#         for i in range(len(s)):
#             if s[i][0] != '#':
#                 ErrorMessage.update(heshteg =  'Тег должен начинаться с # ')
#
#         for i in range(len(s)):
#             if len(s[i]) > 20:
#                 ErrorMessage.update( long = 'Длина тега превышает 20 символов')
#
#         for i in range(len(s)):
#             if s[i][0] == '#' and len(s[i]) == 1:
#                 ErrorMessage.update(one_hesh =  'Хэш-тег состоит из одного символа #')
#
#         for i in range(len(s)):
#             if s[i].count('#') >= 2:
#                 ErrorMessage.update(no_probel = 'Между хэш-тегами отсутствует пробел')
#
#         if len(s) > len(set1):
#             ErrorMessage.update(repeat = 'Повторение хеш-тегов')
#
#         if len(s) > 5:
#             ErrorMessage.update(so_much_hesh = 'Количество тегов превышает 5')
#
#         if len(ErrorMessage) == 0:
#             print('All good!')
#             flag = False
#
#         for value in ErrorMessage.values():
#             print(value)
#     else:
#         print('All good')