subjects = ('ИПО (лаба)',
            'ИПО (лекция)',
            'ОАИП (лаба)',
            'Матем (лекция)',
            'Стандартизация (лекция)',
            'Стандартизация (лаба)',
            'Охрана труда (лекция)',
            'Аловт (практическая)',
            'Аловт (лекция)',
            'Матмод (практическая)')

with open('input.txt', 'r', encoding='utf-8') as file:
    data = file.read()

for word in subjects:
    print(word, data.count(word))
