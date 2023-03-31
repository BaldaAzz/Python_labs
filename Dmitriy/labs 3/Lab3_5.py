s=''
a=int(input('Введите число a: '))
b=int(input('Введите число b: '))
while s!='exit':
    do=input('Выбирете что хотите сделать со значениями: + , - , / , * , stepen , bin , koren ')
    if do=='+':
        do=a+b
        print(do)
        s=input('Чтобы выйти из программы напишите exit')
    elif do=='-':
        do=a-b
        print(do)
        s=input('Чтобы выйти из программы напишите "exit"')
    elif do=='/':
        do=a/b
        print(do)
        s=input('Чтобы выйти из программы напишите "exit"')
    elif do=='*':
        do=a*b
        print(do)
        s=input('Чтобы выйти из программы напишите "exit"')
    elif do=='stepen':
        n=int(input('Введите степень n: '))
        do1=a**n
        print(do1)
        do2=b**n
        print(do2)
        s=input('Чтобы выйти из программы напишите "exit"')
    elif do=='bin':
        do1=bin(a)
        print(a)
        do2=bin(b)
        print(b)
        s=input('Чтобы выйти из программы напишите "exit"')
    elif do=='koren':
        do1=a*0.5
        print(a)
        do2=b*0.5
        print(b)
        s=input('Чтобы выйти из программы напишите "exit"')
        
        
        
