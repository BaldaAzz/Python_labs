run = True

while run:

    print("Введите 2 вещественных числа")
    num1 = float(input('Первое число: '))
    num2 = float(input('Второе число: '))
    print('Выберете операцию: + - * / sqr, sqrt, bin')
    operator = input()

    if operator == '+':
        print(num1, ' + ', num2, ' = ', num1 + num2)
    elif operator == '-':
        print(num1, ' - ', num2, ' = ', num1 - num2)
    elif operator == '*':
        print(num1, ' * ', num2, ' = ', num1 * num2)
    elif operator == '/':
        if num2 != 0:
            print(num1, ' / ', num2, ' = ', num1 / num2)
        else:
            print('Ошибка! На ноль делить нельзя')
    elif operator == 'sqr':
        print(num1,' в квадрате: ', num1**2)
        print(num2,' в квадрате: ', num2**2)
    elif operator == 'sqrt':
        if num1 < 0:
            print('Ошибка! Число должно быть больше либо равно нулю')
        else:
            print('Корень квадратный из числа ', num1,' : ', num1**0.5)
        if  num2 < 0:
            print('Ошибка! Число должно быть больше либо равно нулю')
        else:
            print('Корень квадратный из числа ', num2,' : ', num2**0.5)
    elif operator == 'bin':
        print(num1, ' в двоичной системе счисления: ', bin(int(num1)))
        print(num2, ' в двоичной системе счисления: ', bin(int(num2)))
    
    print('Хотите продолжить?')
    answer = input('да/нет: ')

    if answer == 'нет':
        run = False
        