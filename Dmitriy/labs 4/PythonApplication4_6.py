text = input()
first_word = text[:text.find(' ')]
second_word = text[text.find(' ') + 1:]
print(second_word + ' ' + first_word)
