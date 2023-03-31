import math


def IsPointInRegion(pointX, pointY,):
    """_IsPointInRegion_

    nums:
        pointX (_int_): _coordinat of x for point_
        pointY (_int_): _coordinat of y for point_

    Returns:
        _bool_: _value of key InRegion_
    """
    hypotenuse = math.sqrt((pointX - circleX) ** 2 + (pointY - circleY) ** 2)
    region = not '-' in str(circleR - hypotenuse)  # circleR < hypotenuse
    return region


circleX = int(input('Введите центр по X : '))
circleY = int(input('Введите центр по Y : '))
circleR = int(input('Введите радиус окружности:'))

points = [{'x': 2, 'y': 0, 'InRegion': 'unknown'},
          {'x': -3, 'y': 4, 'InRegion': 'unknown'},
          {'x': 5, 'y': 3, 'InRegion': 'unknown'},
          {'x': 0, 'y': 7, 'InRegion': 'unknown'},
          {'x': -6, 'y': 0, 'InRegion': 'unknown'}
          ]

for i in range(0, len(points)):
    pointX = points[i]['x']
    pointY = points[i]['y']
    points[i].update({'InRegion': IsPointInRegion(pointX, pointY)})

print(points)
