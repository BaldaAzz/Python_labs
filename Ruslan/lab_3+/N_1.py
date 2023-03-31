num1 = int(input('Введите число '))
num2 = int(input('Введите число '))
step = 1

if num2 < num1:
    step = -1
    
for i in range(num1, num2 + step, step):
    print(i)
