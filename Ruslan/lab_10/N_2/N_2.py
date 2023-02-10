numbers = []

with open('numbers.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    for num in data.split():
        numbers.append(int(num))


min_num = min(numbers)
max_num = max(numbers)

with open('min_max_numbers.txt', 'w', encoding='utf-8') as file:
    file.write(str(min_num) + ' ')
    file.write(str(max_num))