from random import randint


class Bank_account:
    account_numbe = ''
    balance = 0

    def __init__(self, account_type):
        self.account_type = account_type
    
    def get_account_numb(self):
        for i in range(16):
            self.account_numbe += str(randint(0, 9))
        
    def get_info_account(self):
        print(self.account_numbe)
        print(self.balance)
        print(self.account_type)

    def put_money(self, summa):
        if summa > 0:
            self.balance += summa
            print('Операриция завершена успешно!')
    
    def withdraw_money(self, summa):
        if summa > self.balance:
            print('У вас недостаточно средств на балансе!')
        else:
            self.balance -= summa
            print('Операриция завершена успешно!')
    
