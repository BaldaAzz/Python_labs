file = open("labs 10/10_2/input.txt", "r")
output = open("labs 10/10_2/output.txt", "w")
lst = []
lst1 = []

for i in file.read().split():
    lst.append(i)
    
max1 = max(lst)
min1 = min(lst)
min1 = str(min1)
max1 = str(max1)

lst1.append(min1)
lst1.append(max1)
file.close()

lst1 = str(lst1)
output.write(lst1)
output.close()
