
class BankAccount:
    def get_info(self):
        with open('V:/_/Информационное отделение/ССО/39 ТП/Сабанцев Даниил Янович/data.txt', 'r') as fileR:
            account_data = fileR.read()
        login = account_data.split()[0]
        deposit = account_data.split()[1]
        dep_type = account_data.split()[2]
        return {'login': login , 'deposit' : deposit , 'type' : dep_type}
        
    def __init__(self):
        self.login = self.get_info()['login']
        self.deposit = int(self.get_info()['deposit'])
        self.type = self.get_info()['type']


    def get_deposit(self, req_dep):
        print('\n'*10)
        if req_dep < self.deposit:
            if req_dep > 0:
                self.deposit -= req_dep
                with open('V:/_/Информационное отделение/ССО/39 ТП/Сабанцев Даниил Янович/data.txt', 'w') as fileW:
                    fileW.write(f'{self.login} {self.deposit} {self.type}')
                print('Успешно')
            else:
                print('Отрицательное значение')
        else:
            print('Недостаточно средств')

    def add_deposit(self, add_dep):
        print('\n'*10)
        if add_dep > 0:
            self.deposit += add_dep
            with open('V:/_/Информационное отделение/ССО/39 ТП/Сабанцев Даниил Янович/data.txt', 'w') as fileW:
                fileW.write(f'{self.login} {self.deposit} {self.type}')
            print('Успешно')
        else:
            print('Отрицательное значение')

    def get_balance(self):
        print('\n'*10)
        print( f'Баланс: {self.deposit}')
         
user = BankAccount()
key = 0
print('\n'*10)
while key != 5:
    print('1-Снятие \n2-Зачисление \n3-Баланс \n4-Данные \n5-Выход')
    key = int(input('Выбор операции: '))
    if key == 1:
        user.get_deposit(int(input('Снятие: ')))
    if key == 2:
        user.add_deposit(int(input('Зачислить: ')))
    if key == 3:
        user.get_balance()
    if key == 4:
        print('\n'*10)
        print(f'Номер счета: {user.get_info()["login"]}\n'
              f'Тип счета: {user.get_info()["type"]}')
    if 0 < key > 5:
        print('\n'*10)
        print(f'Операции ({key}) не существует')
        