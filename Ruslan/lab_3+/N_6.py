num = int(input("Введите число меньше 100: "))

summ = 0

for i in range(1, num + 1):
    summ += 1 / i

print(summ)