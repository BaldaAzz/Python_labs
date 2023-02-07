import random 

a=[]

n=int(input('dlina masiva = '))

for i in range(0, n, 1):
    n = random.randint(-10, 10)
    a.append(n)

print(a, ' ')

sch = 1
otrsum = 0
minel = 11
minpoz = 0

for i in range(0, n, 1):
    if a[i] < 0 :
        otrsum = otrsum + a[i]
    if a[i] < minel:
        minel = a[i]
        minpoz = i

print(minpoz, ' poz min element and = ', minel)
print(otrsum, ' summa otr')

a[minpoz] = otrsum / sch

print(a, ' ')
