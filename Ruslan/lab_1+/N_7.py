a = float(input("Введите а: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
d = float(input("Введите d: "))
k = float(input("Введите k: "))
f = float(input("Введите f: "))

y1 = abs((a**2 / b**2 + c**2 * a**2) / (a + b + c * (k - a / b**3)) + c + (k / b / - k / a) * c )

y2 = abs(((a**2 - b**3 - c**3 * a**2) * (b - c + c * (k - d / b**3)) - (k / b - k / a) * c)**2 - 20000)

y3 = abs(1 - a * b**c - a * (b**2 - c**2) + (b - c + a ) * (12 + b ) / (c - a))

y4 = abs(a - b * c * d**3 + (c**5 - a**2) / a + f**3 * (a - 213))

print("Первое выражение равно: ", y1)
print("Второе выражение равно: ", y2)
print("Третье выражение равно: ", y3)
print("Четвёртое выражение равно: ", y4)
