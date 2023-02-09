tuple1 = tuple([i for i in range(0, 6)])
tuple2 = tuple([i for i in range(0, -6, -1)])

tuple3 = tuple1 + tuple2

print(tuple3)
print(f'Количество 0: {tuple3.count(0)}')