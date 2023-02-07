import math
P=3.14
x=int(input('задайте х '))
if x>=5:
    y2=3*x**2+x-10
    print('y2 = ', y2)
elif x==0:
    y2=math.cos(2*x)+9
    print('y2 = ', y2)
elif (-9<x) and (x<-2):
    y2=x**3+2
    print('y2 = ', y2)    
else:
    y2=1
    print('y2 = ', y2)
