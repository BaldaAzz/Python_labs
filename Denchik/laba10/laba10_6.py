with open('ex_6.txt', 'r') as f:
    s = f.read()
s = s.split()

d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

with open('example6.txt', 'w', encoding='utf-8') as file:
    file.writelines(f"Лекций: {d.get('(лекц.)')}\n")
    file.writelines(f"Практических: {d.get('(практ.)')}")
