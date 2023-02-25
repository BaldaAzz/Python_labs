word = str(input())
flip_word= word[::-1]
if word == flip_word:
  print("Является «перевертышем»")
else:
  print("Не является «перевертышем»")