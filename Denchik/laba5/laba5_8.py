a = [1, 1, 2, 3, 5, 8, 13, 5, 89, 3, 21, 34, 55, 89]
a1 = []

for i in range(len(a)):
    if a.count(a[i]) > 1:
        a1.append(a[i])
        
print(set(a1))