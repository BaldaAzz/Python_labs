text = []
dictionary = {}

''' Любой текст
st = []

while st != ['']:
    st = input(':').split(' ')
    for y in range(len(st)):
        text.append(st[y])
text.pop(-1)
'''

''' По примеру
for i in range(9):
    st=input(':').split(' ')
    for y in range(len(st)):
        text.append(st[y])

print()
'''

for word in text:
    if dictionary.get(word, 0):
        dictionary[word] += 1
    else:
        dictionary[word] = 1

dict_sorted = dict(sorted(dictionary.items(), key=lambda x: x[0]))
for i in dict(sorted(dict_sorted.items(), key=lambda x: x[1], reverse=True)):
    print(i)
