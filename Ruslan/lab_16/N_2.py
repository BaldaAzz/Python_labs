def start_func(func):
    def warper():
        print('Запуск функции')
        func()
    return warper

def finish_func(func):
    def warper():
        func()
        print('Функция выполнена')
    return warper

@start_func
def launch_func():
    print('Функция запущена')

@finish_func
def calculate():
    print('Производятся вычисления…')

@start_func
@finish_func
def process_func():
    print('Функция в процессе выполнения, ожидайте…')

launch_func()
print()
calculate()
print()
process_func()