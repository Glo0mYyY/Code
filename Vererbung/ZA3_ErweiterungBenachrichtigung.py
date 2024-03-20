from A3_Vererbung import SavingsAccount


class NotifyingSavingsAccount(SavingsAccount):
    def __init__(self, schwellenwert):
        super().__init__()
        self.schwellenwert = schwellenwert

    def benachrichtigen(self):
        if self.balance > self.schwellenwert:
            print("Das Guthaben des Kontoinhabers hat den Schwellenwert überschritten.")


sparkonto = NotifyingSavingsAccount(schwellenwert=1000)
sparkonto.deposit(1000)
sparkonto.benachrichtigen()
sparkonto.get_balance()
sparkonto.deposit(1000)
sparkonto.benachrichtigen()
