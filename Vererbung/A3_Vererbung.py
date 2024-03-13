class SavingsAccount:
    def __init__(self):
        self.balance = 0
        self.interest_rate = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('Insufficient funds')
    def set_interest_rate(self, rate):
        self.interest_rate = rate

    def add_interest(self):
        self.balance *= (1 + self.interest_rate)

    def get_balance(self):
        print (self.balance)

class FeeSavingsAccount(SavingsAccount):
    def __init__(self):
        super().__init__()
        self.fee = 0.01

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount + (amount * self.fee)
            print('Withdrawal fee: ', amount * self.fee, 'Withdrawal amount:')
        else:
            print('Insufficient funds')

sparkonto = SavingsAccount()
sparkonto.deposit(1000)
sparkonto.set_interest_rate(0.05)
sparkonto.get_balance()
sparkonto.add_interest()
sparkonto.get_balance()

gebuehrenkonto = FeeSavingsAccount()
gebuehrenkonto.deposit(1000)
gebuehrenkonto.set_interest_rate(0.05)  
gebuehrenkonto.get_balance()
gebuehrenkonto.add_interest()
gebuehrenkonto.get_balance()
gebuehrenkonto.withdraw(100)
gebuehrenkonto.get_balance()