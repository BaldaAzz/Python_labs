def decorator(func):
    def warper():
        print('Запуск функции')
        func()
        print('Функция выполнена')
    return warper

@decorator
def process_information():
    print('Функция в процессе выполнения, ожидайте…')

process_information()