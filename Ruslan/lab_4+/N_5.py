word = input()

reverse_word = word[::-1]

if word == reverse_word:
    print("Слово", word, "- превёртыш")
else:
    print("Слово", word, "- не превёртыш")    