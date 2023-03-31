
I = int(input('Введите количетсво строк : '))
J = int(input('Введите количество столбцов : '))
MaxI = 0
MaxJ = 0
Mass = []
max = -1000
N = 0
  
while N != I :
  
    print('Заполнение строки', N + 1)
    Mass.append(list (map (int, input().split())))
    if len(Mass[ N ]) != J :
        print(f'Напишите [{J}] переменных через пробел')
        Mass.pop( N ) 
    else:
        N += 1
        
print()
  
for I in range ( len(Mass) ):
    for J in range ( len(Mass[ I ]) ):
        
        if Mass[ I ][ J ] > max:
            max = Mass[ I ][ J ]
            MaxI = I + 1
            MaxJ = J + 1

    print(Mass[ I ])
    
print()    

print(f'Максимальный {max}, строка  {MaxI}, столбец  {MaxJ}')               
