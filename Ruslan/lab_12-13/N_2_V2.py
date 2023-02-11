from random import randint


class Bank_account:
    def __init__(self, account_type):
        self.account_type = account_type
        self.account_numbe = ''.join([str(randint(0, 10)) for i in range(16)])
        self.balance = 0
        

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



a_account = Bank_account('deposit')
a_account.get_info_account()
a_account.put_money(1500)
a_account.withdraw_money(100000)
a_account.withdraw_money(15)
a_account.get_info_account()