def decorator(func):
    def warper():
        print('Запуск функции')
        func()
        print('Функция выполнена')

@decorator
def process_information():
    print('Функция в процессе выполнения, ожидайте…')

process_information()