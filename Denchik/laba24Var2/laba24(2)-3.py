"""Задан одномерный массив размерностью 10. 
Переформатировать в двумерныймассив.
Элементы главной диагонали заменить на 0."""

import numpy as np

mass = np.arange(10, dtype=int)
mass = mass.reshape(2,5)

print(mass)

np.fill_diagonal(mass, 0)

print(mass)
