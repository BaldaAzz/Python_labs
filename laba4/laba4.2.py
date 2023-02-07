st = str(input('Ввод строки:'))

x = len(st)
x1 = x%2
x2 = x//2

if x1 != 0:
    x2 = x2 + 1

st1 = st[0: x2]
st2 = st[x2 :x]    

print('Первое ',st1,' Второе', st2)
print(st2 + st1)
