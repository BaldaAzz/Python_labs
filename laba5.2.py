a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Usl1 = 0
Usl2 = 0
Usl3 = 0

for i in range (0, len(a), 1):
    if 4 > a[i] > 0 :
        Usl1 = Usl1 + 1
    if 3 < a[i] < 7 :
        Usl2 = Usl2 + 1
    if 6 < a[i] <10 :
        Usl3 = Usl3 + 1

print('from 1 to 3 = ', Usl1)
print('from 4 to 6 = ', Usl2)
print('from 7 to 9 = ', Usl3)
