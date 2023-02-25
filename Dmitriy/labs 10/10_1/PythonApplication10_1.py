file = open('labs 10/10_1/input.txt', 'r')
stroka = ''

for i in file.read():
    stroka += str(i)

stroka = sorted (stroka)

output = open('labs 10/10_1/output.txt', 'w')

for i in stroka:
    output.write(i)
    
file.close()
output.close()
