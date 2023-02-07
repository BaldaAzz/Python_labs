with open('laba10/ex_1.txt', 'r') as f:
    s = f.read()
    
line = s.count('\n') + 1
word = s.count(' ') + line
s = s.replace('\n', ' ')
s = s.replace(' ', '')
letter = len(s)

print(f'Input file contains: \n{letter} letters \n{word} words'
      f' \n{line} lines ')
