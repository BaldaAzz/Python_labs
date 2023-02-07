st1=[]
i=0
while i<5:
    st1.append(str(input('vvod # :')))
    pr=int(0)              
    if st1:
        pr=pr+1
    if len(st1[i])>1:
        pr=pr+1    
    print(pr)
    if st1[i]:
        print (st1)
        i=i+1
    else: i=5
    pr=int(0)

