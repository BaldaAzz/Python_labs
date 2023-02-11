def check_password(func):
    def warper():
        password = input()
        if password == '1111':
           print(func())
        else:
            print('В доступе отказано')
    return warper

@check_password
def get_sum(N):
    return sum([i for i in range(N)])

get_sum()
