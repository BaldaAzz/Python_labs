import math
a=int(input('введите а = '))
b=int(input('введите b = '))
c=int(input('введите c = '))
D=b**2-4*a*c
if D>0 :
    x1=(-b-math.sqrt(D))/(2*a)
    x2=(-b+math.sqrt(D))/(2*a)
    print('корни')
    print('x1= ',x1)
    print('x2= ',x2)
elif D==0 :
    x=-b/(2*a)
    print('корень')
    print('x =' ,x)
else:
    print('нет корней')
