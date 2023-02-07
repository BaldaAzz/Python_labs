with open('laba10/ex_1.txt', 'r') as f:
    s = f.read()
s = s.split()

print(s)
a = []

for i in s:
    if i.isdigit():
        a.append(int(i))

print(a)
proizv = 1

for i in range(len(a)):
    proizv *= a[i]
print(proizv)

with open('laba10/output.txt', 'w', encoding='utf-8') as file:
    file.writelines(f'Произведение: {proizv}')
