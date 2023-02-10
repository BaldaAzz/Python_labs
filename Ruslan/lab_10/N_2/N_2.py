file_numbers = open('numbers.txt', 'r')

numbers = []

data = file_numbers.read()
for num in data.split():
    numbers.append(int(num))

file_numbers.close()


min_num = min(numbers)
max_num = max(numbers)

min_max_numbers = open('min_max_numbers.txt', 'w')

min_max_numbers.write(str(min_num) + ' ')
min_max_numbers.write(str(max_num))

min_max_numbers.close()