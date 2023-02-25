slov = {}              
text = []     
st = []

while st != ['']:
    st = input('/').split(' ')
    for y in range(len(st)):
        text.append(st[y])
text.pop(-1)

for j in text:           
    slov[j] = slov.get(j, 0) + 1
        
for j in sorted(slov.items(), key = lambda x: (-x[1],x[0])): 
    print(j[0]) 
