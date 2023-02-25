def check_password(func):
    def wrapper(password, N):
        if password == '1111':
           return func(N)
        else:
            print('В доступе отказано')
    return wrapper

@check_password
def get_sum(N):
    return sum([i for i in range(N)])

print(get_sum(input(), 15))
