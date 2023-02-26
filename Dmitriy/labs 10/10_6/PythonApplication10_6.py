file = open('input.txt', 'r')
s = file.read()
words = s.split()

d = {}

for i in words:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
        
y = d.items()

for it in y:
    print(it)

file.close()



