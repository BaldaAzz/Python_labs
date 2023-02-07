points = [
    {'x': 2, 'y': 0, 'inRegion': 'unknown'},
    {'x': -3, 'y': 4, 'inRegion': 'unknown'},
    {'x': 5, 'y': 3, 'inRegion': 'unknown'},
    {'x': 0, 'y': 7, 'inRegion': 'unknown'},
    {'x': -6, 'y': 0, 'inRegion': 'unknown'}
]


def isPointInRegion(point_x, point_y, length, start_x=0, start_y=0, figure='square'):
    result = False

    if figure == 'square':
        x = length / 2
        y = x
        return (x >= point_x and -x <= point_x) and (y >= point_y and -y <= point_y)

    elif figure == 'circle':
        return (point_x - start_x)**2 + (point_y - start_y)**2 <= length**2

def show_dict(point_dict):
    for point in point_dict:
        print(point, end='\n')

lenth_square = 5
radius = 5

x0, y0 = 3, -2

for i in points:
    i['inRegion'] = isPointInRegion(i['x'], i['y'], lenth_square)

show_dict(points)
print()

for i in points:
    i['inRegion'] = isPointInRegion(i['x'], i['y'], radius, figure='circle')

show_dict(points)
print()

for i in points:
    i['inRegion'] = isPointInRegion(i['x'], i['y'], radius, x0, y0, figure='circle')

show_dict(points)