lst = list(map(int, input().split()))
earlier = set()

for i in lst:
    if i in earlier:
        print('YES', end=' ')
    else:
        print('NO', end=' ')
        earlier.add(i)