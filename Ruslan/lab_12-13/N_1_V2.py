class Bank:

    def __init__(self, amount, years):
        self.amount = amount
        self.years = years

    def make_contribution(self):
        persent = 0.1

        for i in range(self.years):
            self.amount += self.amount * persent

        return self.amount


bank = Bank(155, 20)
print(bank.make_contribution())
