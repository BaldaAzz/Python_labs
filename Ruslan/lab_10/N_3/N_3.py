from math import prod

numbers = []

with open('input.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    for num in data.split():
        numbers.append(int(num))

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(str(prod(numbers)))
