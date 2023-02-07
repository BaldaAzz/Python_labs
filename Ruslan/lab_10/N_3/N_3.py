from math import prod

file_input = open(r'C:\Users\Кардан\Desktop\Лабараторные\\ИПО\1 семестр\lab_10\N_3\input.txt', 'r')
data = []
numbers = []

data = file_input.read()
for num in data.split():
    numbers.append(int(num))
file_input.close()

file_output = open(r'C:\Users\Кардан\Desktop\Лабараторные\ИПО\1 семестр\lab_10\N_3\output.txt', 'w')
file_output.write(str(prod(numbers)))
file_output.close()