text = input("Введите текст ")
half_1 = text[:int((len(text)+1)/2)]
half_2 = text[int((len(text)+1)/2):]
print(half_2 + half_1)
