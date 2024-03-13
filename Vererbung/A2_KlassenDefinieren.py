class BankAccount: 
    """Bank Account protected by a pin number."""

    def __init__(self, pin): 
        """Initial account balance is 0 and pin is 'pin'."""
        self.balance = 0
        self.pin = pin
        self.pin_attempts = 0
        self.locked = False

    def deposit(self, amount): 
        """Increment account balance by amount and return new balance."""
        if self.locked:
            print("Account locked.")
        else:
            self.balance += amount
            print("amount deposited: ", amount, "balance: ", self.balance, "CHF.")

    def withdraw(self, amount): 
        """Decrement account balance by amount and return amount withdrawn."""
        if self.locked:
            print("Account locked.")
        else:
            if amount > self.balance and self.locked:
                print("Insufficient funds.")
            else:
                self.balance -= amount
                print("amount withdrawn: ", amount, "balance: ", self.balance, "CHF.")

    def get_balance(self): 
        """Return account balance."""
        if self.locked:
            print("Account locked.")
        else:
            print (self.balance)

    def change_pin(self, oldpin, newpin): 
        """Change pin from oldpin to newpin."""
        if self.locked:
            print("Account locked.")
        else:
            if self.pin == oldpin:
                self.pin = newpin
                print("Pin changed successfully.")
                self.pin_attempts = 0
            else:
                print("Pin change failed.")
                self.pin_attempts += 1
            if self.pin_attempts > 3:
                print("Account locked.")
                self.locked = True

konto1 = BankAccount(1234)
konto1.deposit(100)
konto1.withdraw(150)
konto1.get_balance()
konto1.change_pin(1234, 4321)
konto1.change_pin(1234, 4321)
konto1.change_pin(1234, 4321)
konto1.change_pin(1234, 4321)
konto1.change_pin(1234, 4321)
konto1.get_balance()
konto1.deposit(100)
konto1.withdraw(150)

# Frage 1:
# Die Balance und der Pin
# Frage 2: 
# Der Benutzer soll über den falschen Pin informiert werden, und wenn es zu oft falsch eingegeben worden ist, den account sperren
# Frage 3:
# Die Transaktion soll blockiert werden
# Frage 4:
# 