import math


def isPointInRegion(pointX, pointY, startX, startY, radius, kube) -> bool:  
    hypotenuse = math.sqrt((pointX - startX) ** 2 + (pointY - startY) ** 2)
    region = (radius >= hypotenuse) & (
              kube / 2 >= abs(pointX)) & (
                kube / 2 >= abs(pointY))
    return region


kubeWidth = 100
x = 0
y = 0
circleR = 100
i = '-1'

print(' 1:kube;\n 2:startx;\n 3:starty;\n 4:rcircle;\n 0:exit.' )

while i != '0':
    i = (input('chose:'))
    if i == '1':
        kubeWidth = int(
            input('Введите сторону квадрата:'))
    if i == '2':
        x = int(input('Введите центр по X : '))
    if i == '3':
        y = int(input('Введите центр по Y : '))
    if i == '4':
        circleR = int(
            input('Введите радиус окружности:'))

points = [{'x': 2, 'y': 0, 'InRegion': 'unknown'},
          {'x': -3, 'y': 4, 'InRegion': 'unknown'},
          {'x': 5, 'y': 3, 'InRegion': 'unknown'},
          {'x': 0, 'y': 7, 'InRegion': 'unknown'},
          {'x': -6, 'y': 0, 'InRegion': 'unknown'}
          ]

for i in range(len(points)):
    pointX = points[i]['x']
    pointY = points[i]['y']
    points[i].update({'InRegion': isPointInRegion(pointX, pointY, x, y, circleR, kubeWidth)})

print(points)
