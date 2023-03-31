data = input()

word1 = data[0 : data.find(" ") :]
word2 = data[data.find(" ") + 1 ::]

print(word2 + " " + word1)