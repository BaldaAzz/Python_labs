def replase_data(string):
    return string.replace(' ', '').replace('.', '').replace('\n', '')

file_input = open('input.txt', 'r')
data = file_input.read()
file_input.close()

lines = data.count('\n')
words = len(data.split())
letters = len(replase_data(data))


file_output = open('output.txt', 'w')
file_output.write('Input file contains:\n')
file_output.write(str(letters) + ' letters\n')
file_output.write(str(words) + ' words\n')
file_output.write(str(lines) + ' lines')
file_output.close()
