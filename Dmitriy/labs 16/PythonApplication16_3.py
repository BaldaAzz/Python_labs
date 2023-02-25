def check_password(fn):
    def wrapper():
        pasword = int(input("введите пароль:"))
        if pasword == 1111:
            fn()
        else:
            print("В доступе отказано")
            return None 
    return wrapper

@check_password
def calculate():
    n = int(input("Введите N:"))
    i = 0
    while i < n:
        n += i
        i += 1

calculate()