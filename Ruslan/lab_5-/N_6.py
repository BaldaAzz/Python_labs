lst = [1, -2, 3, -4, 7, 4, -12, -1, 15, -1, -1, 5]
count = 0
multi = 1

for item in lst:
    if item > 0:
        count += 1
        if count == 1 or count == 3 or count == 6:
            multi *= item

print(multi)