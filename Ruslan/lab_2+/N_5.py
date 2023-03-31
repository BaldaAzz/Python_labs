a = int(input("Введите а: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

D = b**2 - 4 * a * c

if D > 0:
   x1 = (-b + D**0.5) / (2 * a)
   x2 = (-b - D**0.5) / (2 * a)

   print("x1 =", x1 )
   print("x2 =", x2)
elif D == 0:
   x = -b  / (2 * a)

   print("x =", x)
else:
   print("Нет корней")