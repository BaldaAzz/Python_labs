def check_password(func):
    def wrapper( *arg , password=input('password:')):
        if password == 'root':
           return func(*arg)
        else:
            print('В доступе отказано')
    return wrapper

@check_password
def get_sum(N):
    return sum([i for i in range(N)])

print(get_sum(15))