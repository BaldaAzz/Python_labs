a=int(input('Введите число a: '))
summ=0
proizv=1
while a>0:
    n=a%10
    a=a//10
    if n==0:
        continue
    summ=summ+n
    proizv=proizv*n
print(summ)
print(proizv)
