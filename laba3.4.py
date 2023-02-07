num=int(input('ввод числа'))
znch=0
suma=0
proiz=1
while num>0:
    znch=(num%10)
    num=num//10
    if znch==0:
        suma=suma
        proiz=proiz
    else:
        suma=suma+znch
        proiz=proiz*znch
print(suma,' сумма')
print(proiz,' произведение')
