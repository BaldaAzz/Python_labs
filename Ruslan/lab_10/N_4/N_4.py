def replase_data(string):
    return string.replace(' ', '').replace('.', '').replace('\n', '')

file_input = open(r'C:\Users\Кардан\Desktop\Лабараторные\ИПО\1 семестр\lab_10\N_4\input.txt', 'r')
data = file_input.read()
file_input.close()

lines = data.count('\n')
words = len(data.split())
letters = len(replase_data(data))


file_output = open(r'C:\Users\Кардан\Desktop\Лабараторные\ИПО\1 семестр\lab_10\N_4\output.txt', 'w')
file_output.write('Input file contains:\n')
file_output.write(str(letters) + ' letters\n')
file_output.write(str(words) + ' words\n')
file_output.write(str(lines) + ' lines')
file_output.close()
