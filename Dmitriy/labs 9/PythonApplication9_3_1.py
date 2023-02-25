def IsPointInRegion(pointX, pointY):
    region = (kube / 2 >= abs(pointX)) & (kube / 2 >= abs(pointY))
    return region

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
    print("x:",pointX,"y:",pointY,":",{'InRegion': IsPointInRegion(pointX, pointY)})

   
