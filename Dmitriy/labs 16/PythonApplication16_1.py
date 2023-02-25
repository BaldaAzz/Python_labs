def simple_decore(fn):
    def wrapper():
        print("Запуск функции")
        fn()
        print("Функция выполнена")
    return wrapper

@simple_decore
def launch():
    print("Функция в процессе выполнения, ожидайте…")

launch()
