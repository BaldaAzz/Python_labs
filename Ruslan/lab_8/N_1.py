text = 'один два три четыре пять два три три два'
dict_words = dict()

for word in text.split():
    dict_words[word] = dict_words.get(word, 0) + 1

max_value = max(dict_words.values())
words = set()

for key in dict_words:
    if dict_words[key] == max_value:
        words.add(key)

print(sorted(words)[0])
