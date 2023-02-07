st=str(input('Ввод строки:'))

x=len(st)
x1=st.find('h')
x2=st.rfind('h')

print(st[0:x1]+st[x2+1:x])
