from math import sqrt
a=int(input('Введите сторону А:'))
b=int(input('Введите сторону B:'))
c=int(input('Введите сторону C:'))
p=0.5*(a+b+c)
print('Периметр', p)
s=sqrt(p*(p-a)*(p-b)*(p-c))
print('Площадь', s)