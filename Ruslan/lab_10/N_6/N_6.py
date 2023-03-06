subjects = ('ИПО', 'ОАИП', 'Матем', 'Охрана труда', 'Аловт', 'Матмод', 'Стандартизация')
types_lessons = ('Лекция', 'Лабараторная работа', 'Практическая')
days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота')

with open(r'Ruslan/lab_10/N_6/input.txt', 'r', encoding='utf-8') as file:
   data = file.read()

new_data = data.split(sep='\n')
for day in days:
   new_data.remove(day)
new_data.remove('')
new_data.pop(-1)


lessons = {}

for subject in subjects:
   for type_lesson in types_lessons:
      key = subject + ' ' + type_lesson
      lessons[key] = 0

for item in new_data:
   count_lesson = new_data.count(item)
   lessons[item] = count_lesson


for lesson, count_lesson in lessons.items():
   if lesson != '':
      print(lesson, count_lesson)
