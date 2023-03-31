import math as m
a=int(input('Введите число a: '))
b=int(input('Введите число b: '))
c=int(input('Введите число c: '))
D=0
x1=0
x2=0
x=0
D=b**2-4*a*c
print('Дискриминант = ',D)
if D>0:
    x1=(-b-m.sqrt(D))/(2*a)
    x2=(-b+m.sqrt(D))/(2*a)
    print('Значение x1 = ',x1)
    print('Значение x2 = ',x2)
elif D==0:
    x=m.sqrt(D)/(2*a)
    print('Значение x = ',x)
else:
    print('Введены неправильные параметры')
