import math

def IsPointInRegionSphere(point_x, point_y):
    hypotenuse = math.sqrt(point_x **2 + point_y ** 2) 
    region = r_circle > hypotenuse
    return region

r_circle = int(input('Введите радиус окружности:'))

points = [ {'x': 2, 'y': 0, 'InRegion': 'unknown'},
           {'x': -3, 'y': 4, 'InRegion': 'unknown'},
           {'x': 5, 'y': 3, 'InRegion': 'unknown'},
           {'x': 0, 'y': 7, 'InRegion': 'unknown'},
           {'x': -6, 'y': 0, 'InRegion': 'unknown'}
        ]

for i in range( 0, len(points)):
    point_x=points[ i ] [ 'x' ]
    point_y=points[ i ] [ 'y' ]
    print("x:",point_x,"y:",point_y,":",({'InRegion': IsPointInRegionSphere(point_x, point_y)}))
    


