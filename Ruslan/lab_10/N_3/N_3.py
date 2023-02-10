from math import prod

file_input = open('input.txt', 'r')
data = []
numbers = []

data = file_input.read()
for num in data.split():
    numbers.append(int(num))
file_input.close()

file_output = open('output.txt', 'w')
file_output.write(str(prod(numbers)))
file_output.close()