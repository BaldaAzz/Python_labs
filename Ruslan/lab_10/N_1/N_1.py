data = []
with open('numbers.txt', 'r', encoding='utf-8') as file:
    for number in file:
        data.append(int(number))

data.sort()
with open('sorted_numbers.txt', 'w', encoding='utf-8') as file:
    for number in data:
        file.write(str(number) + '\n')
