with open('laba10/ex_2.txt', 'r') as f:
    s = f.readlines()
print(s)

a = []
[a.append(s[i].split())for i in range(len(s))]

print(a)

with open('laba10/example5.txt', 'w') as file:
    [file.writelines(f"{' '.join(a[i])}\n") for i in range(len(a)) if int(a[i][1])<40]