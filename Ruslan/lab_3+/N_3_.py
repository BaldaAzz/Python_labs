num = int(input("Введите число: "))

count_even_num = 0
count_odd_num = 0

while num > 0:

    value = num % 10

    if value % 2 == 0:
        count_even_num += 1
    else:
        count_odd_num += 1
    
    num = num // 10

print("Количество чётных чисел: ", count_even_num)
print("Количество нечётных чисел: ", count_odd_num) 
