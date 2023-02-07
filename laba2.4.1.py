import math
P=3.14
x=int(input('задайте х '))
if (0<x) and (x>8):
    y3=4*P+x
    print('y = ', y3)
elif x==0:
    y3=2*math.tan(x)+x
    print('y = ', y3)
elif x<0:
    y3=math.sin(x)+9*math.cos(x)
    print('y = ', y3)    
else:
    print('y = ', 0)
