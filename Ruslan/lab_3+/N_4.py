num = int (input("Введите целое число, которое больше 0: "))

if num == 0 or num < 0:
    print("Ошибка")
else:
    sum_num = 0
    multi_num = 1

    while num > 0:
        value = num % 10
        num = num // 10

        if value > 0:
            sum_num += value
            multi_num *= value

print("Сумма цифр равна: ", sum_num)
print("Произведение цифр равно: ", multi_num)
