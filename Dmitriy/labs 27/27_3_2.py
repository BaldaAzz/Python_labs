import pandas as pd
import numpy as np

array = np.array([-6, 5, 21, 20, 3, -7, 14, 9]) 
s = pd.Series(array)

print("основная таблица:\n",s)
print("элементы от 5 до 20:\n", s[(s > 5) & (s < 20)])

s.loc[s.values % 2 == 0 ] = s * 3

print("изменная таблица\n",s)
print("логарифмы:\n",np.log(s))