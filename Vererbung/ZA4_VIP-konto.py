from A3_Vererbung import SavingsAccount

class VIPAccount(SavingsAccount):
    def __init__(self):
        super().__init__()
        self.interest_rate_small = 0.01
        self.interest_rate_medium = 0.02
        self.interest_rate_large = 0.03

    def add_interest(self):
        if self.balance < 1000:
            self.balance *= (1 + self.interest_rate_small)
            print('Interest rate: ', self.interest_rate_small, 'Interest added: ', self.balance * self.interest_rate_small)
        elif self.balance < 5000:
            self.balance *= (1 + self.interest_rate_medium)
            print('Interest rate: ', self.interest_rate_medium, 'Interest added: ', self.balance * self.interest_rate_medium)
        else:
            self.balance *= (1 + self.interest_rate_large)
            print('Interest rate: ', self.interest_rate_large, 'Interest added: ', self.balance * self.interest_rate_large)
print('VIPAccount')
vipkonto = VIPAccount()
vipkonto.get_balance()
vipkonto.deposit(500)
vipkonto.add_interest()
vipkonto.get_balance()
vipkonto.deposit(4000)
vipkonto.add_interest()
vipkonto.get_balance()
vipkonto.deposit(10000)
vipkonto.add_interest()
