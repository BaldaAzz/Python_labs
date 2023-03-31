import math

x = int(input("Введите x: "))

if 0 < x < 8:
   y = 4 * math.pi + x
elif x == 0:
   y = 2 * (math.sin(x) / math.cos(x)) + x
elif x < 0:
   y = math.sin(x) + 9 * math.cos(x)
else:
   y = 0

print("Функция равна: ", y)
