lst = [-1, 13, -45, -25, -24, -37, -17, 2, 3, 15, 26, 0]
summ = 0
count = 0
min_element = lst[0]
index_min = 0

for i in lst:
    if i < 0:
        summ += i
        count += 1

average = summ / count

for i in range(0, len(lst) - 1):
    if min_element > lst[i]:
        min_element = lst[i]
        index_min = i

lst[index_min] = average

print(lst)