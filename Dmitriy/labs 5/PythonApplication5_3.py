lst = [1,3,4,-4,-4,-65,-345,-13,-34,-56,-76]
summa = 0
count = 0

for i in range (len (lst)):
    if lst[i] < 0:
        summa += lst[i]
        count += 1
    if lst[i] == min(lst):
        index = i
  
avarage = (summa / count)
lst[index] = avarage








