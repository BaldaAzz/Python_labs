import numpy as np

lst = np.random.randint(-50,50,72)
print(lst.reshape(8,9))

min = np.argmin(lst)
max = np.argmax(lst)
lst[min],lst[max] = lst[max],lst[min]
lst = lst.reshape(8,9)

print("индекс минимального элемента:",min,' \n индекс макимального элемента',max)
print(lst)
