a = float(input("Введите сторону а: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

P = a + b + c
half_P = P / 2
S = (half_P  * (half_P - a) * (half_P - b) * (half_P - c)) ** 0.5

print("Площадь треугольника равна: ", S)
print('Периметр треугольника равен: ', P)