def choose_an_option(option):
    def simple_decore_1(fn):
        def wrapper():
            if option == 1:
                print("Запуск функции")
                fn()
            if option == 2:
                fn()
                print("Функция выполнена")
        return wrapper
    return simple_decore_1

@choose_an_option(1)
def launch():
    print("Функция запущена")

@choose_an_option(2)
def calculate():
    print("Производятся вычисления…")

@choose_an_option(1)
@choose_an_option(2)
def work():
    print("Функция в процессе выполнения, ожидайте…")

launch()
print()
calculate()
print()
work()
