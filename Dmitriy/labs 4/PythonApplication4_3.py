text = input()
text = text[:text.find('h')] + text[text.rfind('h') + 1:]
print(text)
