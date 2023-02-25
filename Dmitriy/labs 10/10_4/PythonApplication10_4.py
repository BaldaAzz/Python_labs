lines = 0
words = 0
letters = 0
for line in open('labs 10/10_4/input.txt', 'r'):
    lines += 1
    letters += len(line)
    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':  
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
            
print("строк:", lines)
print("слова:", words)
print("буквы:", letters)
