N = int(input("Введите число N: "))

sum_N = 0

for i in range(1, N + 1):
    sum_N += i

print("Сумму натуральных чисел от 1 до ", N, "равна: ",sum_N)