a=int(input('Введите число a: '))
sum1=0
sum2=0
while a>0:
    n=a%10
    a=a//10
    if n%2==0:
        sum1+=1
    else:
        sum2+=1
print('Всего чётных чисел',sum1)
print('Всего нечётных чисел',sum2)
print(a)
print(n)
