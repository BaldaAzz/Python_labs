def replase_data(string):
    for i in (' ', '.', '\n'):
        string.replace(i, '')
    return string

with open('input.txt', 'r', encoding='utf-8') as file:
    data = file.read()

lines = data.count('\n')
words = len(data.split())
letters = len(replase_data(data))


with open('output.txt', 'w', encoding='utf-8') as file:
    file.write('Input file contains:\n')
    file.write(str(letters) + ' letters\n')
    file.write(str(words) + ' words\n')
    file.write(str(lines) + ' lines')

