file = open('labs 10/10_3/input.txt', 'r')
output = open('labs 10/10_3/output.txt', 'w')
lst = []
rezult = 1

for i in file.read().split():
    lst.append(i)

for j in lst:
    rezult *= int(j)
    
rezultstr = str(rezult)
output.write(rezultstr)

file.close()
output.close()
