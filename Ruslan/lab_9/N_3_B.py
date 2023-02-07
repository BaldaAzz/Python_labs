points = [
    {'x': 2, 'y': 0, 'inRegion': 'unknown'},
    {'x': -3, 'y': 4, 'inRegion': 'unknown'},
    {'x': 5, 'y': 3, 'inRegion': 'unknown'},
    {'x': 0, 'y': 7, 'inRegion': 'unknown'},
    {'x': -6, 'y': 0, 'inRegion': 'unknown'}
]


def isPointInRegion(x, y, radius):
    return x**2 + y**2 <= radius**2

radius = int(input('Введите радиус: '))


for point in points:
    point['inRegion'] = isPointInRegion(point['x'], point['y'], radius)

for point in points:
    print(point, end='\n')