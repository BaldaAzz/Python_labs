file_numbers = open(r'C:\Users\Кардан\Desktop\Лабараторные\ИПО\1 семестр\lab_10\N_2\numbers.txt', 'r')

numbers = []

data = file_numbers.read()
for num in data.split():
    numbers.append(int(num))

file_numbers.close()


min_num = min(numbers)
max_num = max(numbers)

min_max_numbers = open(r'C:\Users\Кардан\Desktop\Лабараторные\ИПО\1 семестр\lab_10\N_2\min_max_numbers.txt', 'w')

min_max_numbers.write(str(min_num) + ' ')
min_max_numbers.write(str(max_num))

min_max_numbers.close()