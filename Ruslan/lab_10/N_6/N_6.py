def counting(word):    
    print(word, data.count(word))

subjects = ('ИПО (лаба)',
        'ИПО (лекция)',
        'ОАИП (лаба)',
        'Матем (лекция)',
        'Стандартизация (лекция)',
        'Охрана труда (лекция)',
        'Аловт (практическая)',
        'Аловт (лекция)',
        'Матмод (практическая)',
        'Стандартизация (лаба)'
        )

input_file = open(r'C:\Users\Кардан\Desktop\Лабараторные\ИПО\1 семестр\lab_10\N_6\input.txt', 'r')
data = input_file.read()

for word in subjects:
    counting(word)

input_file.close()
