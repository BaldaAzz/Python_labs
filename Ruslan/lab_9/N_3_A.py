points = [
    {'x': 2, 'y': 0, 'inRegion': 'unknown'},
    {'x': -3, 'y': 4, 'inRegion': 'unknown'},
    {'x': 5, 'y': 3, 'inRegion': 'unknown'},
    {'x': 0, 'y': 7, 'inRegion': 'unknown'},
    {'x': -6, 'y': 0, 'inRegion': 'unknown'}
]


def isPointInRegion(x, y):
    x_max = side / 2
    y_max = x_max
    return (x <= x_max) and (x >= -x_max) and (y <= y_max) and (y >= -y_max)

side = int(input('Введите сторону квадрата: '))






for point in points:
    point['inRegion'] = isPointInRegion(point['x'], point['y'])

for point in points:
    print(point, end='\n')