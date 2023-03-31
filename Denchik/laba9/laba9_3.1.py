
def IsPointInRegion(pointX, pointY):

    Region = not '-' in str(kube / 2 - abs(pointX)  # circleR > hypotenuse
                            ) and not '-' in str(kube / 2 - abs(pointY))
    return Region


kube = int(input('Введите сторону квадрата:'))

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
