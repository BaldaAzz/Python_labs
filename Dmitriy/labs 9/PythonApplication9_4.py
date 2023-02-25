import math

def isPointInRegion(pointX, pointY, startX, startY, radius, kube) -> bool:  
    hypotenuse = math.sqrt((pointX - startX) ** 2 + (pointY - startY) ** 2)
    region = (radius >= hypotenuse) & (kube / 2 >= abs(pointX)) & (kube / 2 >= abs(pointY))
    return region

kube_width = 100
x = 0
y = 0
circler = 100
i = '-1'

print(' 1:квадрат;\n 2:точка Х;\n 3:точка Y;\n 4:круг;\n 0:вывод.' )

while i != '0':
    i = (input('выбор:'))
    if i == '1':
        kube = int(
            input('Введите сторону квадрата:'))
    if i == '2':
        x = int(input('Введите центр по X : '))
    if i == '3':
        y = int(input('Введите центр по Y : '))
    if i == '4':
        circler = int(
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
    print("x:",pointX,"y:",pointY,":",{'InRegion': isPointInRegion(pointX, pointY, x, y, circler, kube_width)})


