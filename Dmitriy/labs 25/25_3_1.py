import numpy as np

size = int(input("введите размер матрицы"))
array1 = np.random.randint(0, 10, (size, size))
array2 = np.random.randint(0, 10, (size, size))
summ1 =  np.sum(array1.T) 
summ2 =  np.sum(array2.T) 
multi = array1 * array2

print("маccсив 1:\n",array1,"\nмаcсив 2:\n",array2)
print("произведение матриц:\n",multi)
print ("сумма первого массива:",summ1,"\n","сумма второго массива:",summ2,"\n")

if summ1 < summ2:
    print("первый массив меньше:",summ1)
else:
    print("второй массив меньше:",summ2)
    