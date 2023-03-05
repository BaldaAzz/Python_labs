import numpy as np

array = np.random.randint(0, 50, (5, 5))

print(array)

uniq = np.unique(array, return_counts = True )[1] == 1

print(np.unique(array)[uniq])
