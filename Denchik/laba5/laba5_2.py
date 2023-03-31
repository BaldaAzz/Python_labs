a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x1 = 0
x2 = 0
x3 = 0

for i in range(0, len(a), 1):
    if 4 > a[i] > 0:
        x1 = x1 + 1
    if 7 > a[i] > 3:
        x2 = x2 + 1
    if 10 > a[i] > 6:
        x3 = x3 + 1

print('1 to 3 =', x1)
print('4 to 6 =', x2)
print('7 to 9 =', x3)
