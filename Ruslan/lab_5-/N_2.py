from random import randint

lst = [1, 5, 38, 9, 7, 5, 6, 7, 2, -5]
count1_3 = 0
count4_6 = 0
count7_9 = 0

for item in lst:
    if item <= 3 and item >= 1:
        count1_3 += 1
    elif item <= 6 and item >= 4:
        count4_6 += 1
    elif item <= 9 and item >= 7:
        count7_9 += 1
        
print(lst)
print('От 1 до 3: ', count1_3,'\nОт 4 до 6: ', count4_6, '\nОт 7 до 9: ', count7_9)