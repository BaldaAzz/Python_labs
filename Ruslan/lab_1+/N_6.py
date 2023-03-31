num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print(num1, " + ", num2, " = ", num1 + num2)
print(num1, " - ", num2, " = ", num1 - num2)
print(num1, " * ", num2, " = ", num1 * num2)

if num2 == 0:
    print("На ноль делить нельзя")
else:
    print(num1, "/", num2, " = ", num1 / num2)
    print("Целочисленное деление чисел ", num1," и ", num2, " : ", num1 // num2)
    
print(num1, " в квадрате равно: ", num1 ** 2)
print(num2, " в квадрате равно: ", num2 ** 2)

print(num1, "в двоичной системе счисления: ", bin(num1))
print(num2, "в двоичной системе счисления: ", bin(num2))

print(num1, "в восмеричной системе счисления: ", oct(num1))
print(num2, "в восмеричной системе счисления: ", oct(num2))

print(num1, "в шесндцатеричной системе счисления: ", hex(num1))
print(num2, "в шеснадцатеричной системе счисления: ", hex(num2))
