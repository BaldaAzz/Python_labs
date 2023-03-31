import random

s = [random.randint(-20,30) for i in range(23)]
s1 = []
kol = 0

print(s)

for i in range(len(s)):
    if s[i] > 0:
        kol += 1
        s1.append(s[i])

print(s1)
print('Первый, третий и шестой элемент списка: ', s1[0],', ', s1[2],', ', s1[5],
      '\nПроизведение элементов равно: ', s1[0]*s1[2]*s1[5])