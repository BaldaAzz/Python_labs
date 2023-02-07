A=int(input('Pervoe chislo: '))
B=int(input('Vtoroe chislo: '))

C=1

if B<A:
    C=-1
    
for i in range (A,B+C,C):
    print(i)
    

