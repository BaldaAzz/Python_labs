x = int(input("Введите x: "))
y = int(input("Введите y: "))

if x > 0 and y > 0:
   print("Точка находится в 1 четверти")
elif x > 0 and y < 0:
   print("Точка находится в 4 четверти")
elif x < 0 and y > 0:
   print("Точка находится в 2 четверти")
elif x < 0 and y < 0:
   print("Точка находится в 3 четверти")
else:
   print("Точка лежит на оси")
