from A3_Vererbung import SavingsAccount


class FlexibleSavingsAccount(SavingsAccount):
    def __init__(self, fee_cap, fee_amount):
        super().__init__()
        self.fee_cap = fee_cap
        self.fee_amount = fee_amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds or withdrawal amount exceeds maximum withdrawal amount')
        elif amount > (self.fee_cap * self.balance):
            self.balance -= amount + self.fee_amount
            print('Withdrawal fee: ', self.fee_amount, 'Withdrawal amount: ', amount)
        elif amount <= (self.fee_cap * self.balance):
            self.balance -= amount
            print('Withdrawal fee: 0', 'Withdrawal amount: ', amount)

print ('FlexibleSavingsAccount')
flexkonto = FlexibleSavingsAccount(fee_cap=0.1, fee_amount=10)
flexkonto.deposit(1000)
flexkonto.get_balance()
flexkonto.withdraw(100)
flexkonto.get_balance()
flexkonto.withdraw(100)
flexkonto.get_balance()
flexkonto.withdraw(1000)