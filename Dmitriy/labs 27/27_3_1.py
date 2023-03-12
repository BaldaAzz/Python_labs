import pandas as pd
import numpy as np

array = np.array([1, 3, -6, 10, -5, 0, 8, 2, 7]) 
s = pd.Series(array, index = ["a", "b", "c", "d", "e", "f", "g", "h", "i"])
mark = s["a"], s["d"], s["e"]
value = s[0], s[3], s[4]

print(s)
print("по метке:", mark)
print("по индексу:", value)
print("элементы больше 3:\n",s[s > 3])

s.loc[s > 0] = 1
s.loc[s < 0] = s * -1
print(s)
