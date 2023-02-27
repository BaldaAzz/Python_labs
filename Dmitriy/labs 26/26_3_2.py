import numpy as np

lst = np.random.randint(0,25, (5,5),int)

print(lst)
individual = np.unique(lst, return_counts = True)
print(individual)