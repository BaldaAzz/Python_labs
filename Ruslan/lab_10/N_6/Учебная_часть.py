from random import randint, choice


subjects = ('ИПО', 'ОАИП', 'Матем', 'Охрана труда', 'Аловт', 'Матмод', 'Стандартизация')
types_lessons = ('Лекция', 'Лаба', 'Практическая')
days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота')


with open(r'Ruslan/lab_10/N_6/input.txt', 'w', encoding='utf_8') as file:
    for day in days:
        file.write(f'{day}\n')
        for lesson in range(randint(1, 5)): 
            file.write(f'{choice(subjects)} {choice(types_lessons)}\n')
        file.write('\n')