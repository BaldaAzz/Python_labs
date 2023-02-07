x=int(input('введите x '))
y=int(input('введите y '))
if x>0 and y>0 :
    print('первая')
elif x<0 and y>0 :
    print('вторая')
elif x<0 and y<0 :
    print('третья')
elif x>0 and y<0 :
    print('четвертая')
else :
    print('одна из точек координат пренадлежит оси')
input()
