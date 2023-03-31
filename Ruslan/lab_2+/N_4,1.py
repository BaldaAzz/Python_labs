x = int(input("Введите x: "))

if x > 0:
   y = 2 * x - 10
elif x < 0:
   y = 2 * abs(x) - 1
else:
   y = 0

print("Функция равна: ", y)