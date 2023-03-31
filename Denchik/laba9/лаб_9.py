# Задание 1



# Задание 2
# arr_in = [12, 23, 34, 45]
# arr_out = []
# def sp():
#     for i in range(len(arr_in)):
#         summa = 0
#         while arr_in[i] > 0:
#             summa += arr_in[i] % 10
#             arr_in[i] //= 10
#         arr_out.append(summa)
#     print(arr_out)
# sp()


# Задание 3
# Дан список, содержащий 5 точек с координатами на плоскости.
# Определить, принадлежит ли каждая точка
# А) квадрату со стороной N с «центром» в начале координат
# points = [{'x': 2, 'y': 0, 'inRegion': 'unknown'},
#           {'x': -3, 'y': 4, 'inRegion': 'unknown'},
#           {'x': 5, 'y': 3, 'inRegion': 'unknown'},
#           {'x': 0, 'y': 7, 'inRegion': 'unknown'},
#           {'x': -6, 'y': 0, 'inRegion': 'unknown'}]
#
# def IsPointInSquare(x, y):
#     return (1 >= x >= -1) and (-1 <= y <= 1)
#
# for_x = []
# for_y = []
# x_y = [for_x, for_y]
# for i in range(len(points)):
#     for k, v in points[i].items():
#         if k == 'x' :
#             for_x.append(v)
#         elif k =='y':
#             for_y.append(v)
# print(x_y)
# for i in range(len(x_y)):
#     for j in range(len(x_y[i])):
#         print(x_y[i][j], end=' ')
#     print()


# for_x = []
# for_y = []
# x_y = [for_x, for_y]
# for i in range(len(points)):
#     for k, v in points[i].items():
#         if k == 'x' :
#             for_x.append(v)
#         elif k =='y':
#             for_y.append(v)



