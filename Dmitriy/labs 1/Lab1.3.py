import math as mt
a=int(input("Введите a="))
b=int(input("Введите b="))
c=int(input("Введите c="))
p=1/2*(a+b+c)
print("p=",p)
S=mt.sqrt(p*(p-a)*(p-b)*(p-c))
print("S=",S)
