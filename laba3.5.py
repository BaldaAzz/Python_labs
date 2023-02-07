import math
ts=str()
num1=int(input('vvod chislo '))
while ts!='=':
    print('Chose task[+,-,*,/,bin,sqr,sqrt,=]')
    ts=str(input())
    if ts == '+':
        num2=int(input('vvod chislo '))
        num=num1+num2
        print(num1,ts,num2,'=',num)
    elif ts == '-':
        num2=int(input('vvod chislo '))
        num=num1-num2
        print(num1,ts,num2,'=',num)
    elif ts == '*':
        num2=int(input('vvod chislo '))
        num=num1*num2
        print(num1,ts,num2,'=',num)
    elif ts == '/':
        num2=int(input('vvod chislo '))
        num=num1/num2
        print(num1,ts,num2,'=',num)
    elif ts == 'bin':    
        print(bin(num1))
        num=num1
    elif ts == 'sqr':
        num=num1**2
        print(num)
    elif ts == 'sqrt':
        num=math.sqrt(num1)
        print(num)
    elif ts=='=':
        print('Last number', num1)
    else:
        print('Sintax eror ["',ts,'"] Not found')
        print('try again')
    num1=num
print('End of work')

    
