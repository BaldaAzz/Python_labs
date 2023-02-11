n = input('Введите текст: ').split()

dictionary = {}

for word in n:
    if dictionary.get(word, 0):
        dictionary[word] += 1
    else:
        dictionary[word] = 1
        
m = max(dictionary.values())
dict_sorted = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
print(list(dict_sorted.keys())[0])