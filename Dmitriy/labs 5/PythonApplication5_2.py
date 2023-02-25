lst = [1,2,3,6,1,5,3,1,5,3,39,6,3,7]
numbers_1 = 0
numbers_2 = 0
numbers_3 = 0

for i in lst:
    if (i >= 1) and (i <= 3):
        numbers_1 += 1
    elif (i >= 4) and ( i<= 6):
        numbers_2 += 1
    elif (i >= 7) and (i <= 9):
        numbers_3 += 1
        
print('Количество значений от 1 до 3:', numbers_1)
print('Количество значений от 4 до 6:', numbers_2)
print('Количество значений от 7 до 9:', numbers_3)

