with open('laba10/ex_2.txt', 'r') as f:
    s = f.read()
s = s.split()

print(s)

a = []
for i in s:
    if i.isdigit():
        a.append(int(i))

a_min = min(a)
a_max = max(a)

print(a_max, a_min)

with open('laba10/example2.txt', 'w') as file:
    file.write(f'Max:  {a_max} \nMin: {a_min}')
