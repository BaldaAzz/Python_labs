dictionary = {}
text = []
st = []

while st != ['']:
    st = input('/').split(' ')
    for y in range(len(st)):
        text.append(st[y])
text.pop(-1)

for i in text:
    if dictionary.get(i, 0):
        dictionary[i] += 1
    else:
        dictionary[i] = 1
        
dict_sorted = dict(sorted(dictionary.items(), key = lambda x: x[1]))
dict_sorted = dict(sorted(dict_sorted.items(), key = lambda x: x[-1]))

print("самое часто встречаемое слово:",list(dict_sorted.keys())[-1])
