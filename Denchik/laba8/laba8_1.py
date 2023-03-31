text = input('Введите текст: ').split()
dictionary = {}

for word in text:
    if dictionary.get(word, 0):
        dictionary[word] += 1
    else:
        dictionary[word] = 1

dict_sorted = dict(sorted(dictionary.items(), key=lambda x: x[0]))
dict_sorted = dict(sorted(dict_sorted.items(), key=lambda x: x[1], reverse=True))

print(list(dict_sorted.keys())[0])