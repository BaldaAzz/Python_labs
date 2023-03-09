import numpy as np

array = np.random.randint(0, 50, (5, 5))

print(array)

uniq = np.unique(array, return_counts = True )

print("неповторяющиеся элементы:",uniq[0][uniq[1] == True])
