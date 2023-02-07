num1=int(input('ввод числа:'))

chet=0
nechet=0

while num1>0:
    ost=num1%2
    num1=num1//10
    if ost==0 :
        chet=chet+1
    else:
        nechet=nechet+1

print(chet,' четных')
print(nechet,' нечетных')
    
