num1=int(input('Введите переменную 1 : '))
num2=int(input('Введите переменную 2 : '))
znch=hex(num1+num2)
print('сумма ',znch)
znch=oct(num1-num2)
print('вычетание ',znch)
znch=bin(num1*num2)
print('умножение ',znch)
znch=(num1//num2)
print('целочисленное деление ',znch)
znch1=num1**3
znch2=num2**3
print('возведение в куб ',znch1 ,"&", znch2)