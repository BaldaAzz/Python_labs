with open('laba10/ex_1.txt', 'r') as f:
    s = f.read()
    s = s.replace('\n', ' ')
s = s.split()

print(s)

a = []
for i in s:
    if i.isdigit():
        a.append(int(i))
a.sort()

print(a)

with open('laba10/example1.txt', 'w') as file:
    for i in range(len(a)):
        file.writelines(f'{a[i]}\n')
