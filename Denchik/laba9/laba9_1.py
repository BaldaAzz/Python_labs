def sdvig(lst, step):  # In left
    step = abs(step)
    for i in range(step):
        lst.insert(len(lst), lst.pop(0))



def sdvig(lst, step):  # In right
    
    step = abs(step)
    for i in range(step):
        lst.insert(0, lst.pop(-1))


num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input('Введите количество шагов: '))

print(num)

sdvig(num, n)
print(num)
