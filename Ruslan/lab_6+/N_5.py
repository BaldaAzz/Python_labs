colline = list(map(int, input().split()))
lst = []
max_elem = 0
index_list = [0, 0]

n, m = int(colline[0]), int(colline[1])

for i in range(n):
    line = input().split()
    for j in range(len(line)):
        line[j] = int(line[j])
    lst.append(line)

for i in range(m):
    for j in range(n-1, -1, -1):
        print(lst[j][i], end=' ')
    print()

