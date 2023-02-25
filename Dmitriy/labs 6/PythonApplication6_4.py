lst = []
for i in input().split():
    lst.append(i)
n = int(lst[0])
m = int(lst[1])
lst1 = []
i_max = 0
j_max = 0

print('вывидите построчно ваши элементы матрицы ')

for i in range(n):
    lst1.append(list(map(int,input().split())))
    
for i in range(n):
    for j in range(m):
        if lst1[i][j] > lst1[i_max][j_max] :
            i_max = i
            j_max = j
            
print(i_max,j_max)
