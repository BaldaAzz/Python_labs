import numpy as np

size = int(input("введите размер матрицы"))
lst1 = np.random.randint(0,10, (size,size))
lst2 = np.random.randint(0,10, (size,size))
summ1 =  np.sum(lst1.T) 
summ2 =  np.sum(lst2.T) 
multi = lst1 * lst2
print(lst1,"\n///////////////////\n",lst2)
print("///////////////произведение матриц\n",multi)
print ("сумма первого массива",summ1,"\n///////////////////\n","сумма второго массива",summ2,"\n////////")
if summ1 < summ2:
    print("первый массив меньше:",summ1)
else:
    print("второй массив меньше:",summ2)