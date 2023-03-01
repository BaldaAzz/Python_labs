a = int(input('введите шаг:'))
lst = [1,3,4,5,6,2,3,5,4,3,67]

def walk(lst,steps):
    
    steps %= len(lst)
    steps = abs(steps)
    for i in range(steps):
       lst.append(lst.pop(0))
        
print("исходный список:",lst)
walk(lst,a)
print("измененый список:",lst)
