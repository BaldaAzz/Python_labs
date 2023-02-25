lst = [-8, 3, 1, -3, 4, -3, -9, 0, 2, -4, 4, -1, -3, -6, -5, -6]
counter = 0
i = 0
mult = 1

for i in range(len (lst)):
    if lst[i] > 0:
        counter += 1
        if counter == 1 or counter == 3 or counter == 6:
            mult *= lst[i]
    i+=1

print(lst)
print("Произведение:", mult)  
