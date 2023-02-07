file_numbers = open(r'C:\Users\Кардан\Desktop\Лабараторные\ИПО\1 семестр\lab_10\N_1\numbers.txt', 'r')
data = []

for number in file_numbers:
    data.append(int(number))

file_numbers.close()


data.sort()
file_sorted_numbers = open(r'C:\Users\Кардан\Desktop\Лабараторные\ИПО\1 семестр\lab_10\N_1\sorted_numbers.txt', 'w')

for number in data:
    file_sorted_numbers.write(str(number) + '\n')

file_sorted_numbers.close()