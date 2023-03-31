import math

x = int(input("Введите x: "))

if x >= 5:
   y = 3 * x**2 + x - 10
elif -9 < x  < -2:
   y = x**3 + 2
elif x == 0:
   y = math.cos(2 * x) + 9
else:
   y = 1

print("Функция равна: ", y)