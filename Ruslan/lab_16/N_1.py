def decorator(func):
    def wrapper():
        print('Запуск функции')
        func()
        print('Функция выполнена')
    return wrapper

@decorator
def process_information():
    print('Функция в процессе выполнения, ожидайте…')

process_information()