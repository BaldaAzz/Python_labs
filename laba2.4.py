import math
P=3.14
x=int(input('задайте х '))
if x>0:
    y1=2*x-10
    print('y = ', y1)
elif x==0:
    y1=0
    print('y = ', y1)
else:
    y1=2*abs(x)-1
    print('y = ', y1)

