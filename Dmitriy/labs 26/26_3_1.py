import numpy as np

lst = np.array(np.arange(-5,10),int)
    
zero = list(lst).index(0)

print(lst)

lst.sort()
print("отрицательных элементов:",len(lst[0:zero]))
print("положительных элементов:",len(lst[zero + 1:]))
print("нулевых элементов:",len(lst[zero:zero + 1]))