dict_words = {}  

for i in range(int(input())):
    text = input().split()

    for word in text:           
        dict_words[word] = dict_words.get(word, 0) + 1

for word in sorted(dict_words.items(), key=lambda x: (-x[1],x[0])): 
    print(word[0]) 
