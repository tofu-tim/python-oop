class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds.")
            print("Current balance:", str(self.balance))
        else:
            self.balance = (self.balance - amount)
        return self.balance
    def display_account_info(self):
        print(self.balance)

    def yield_interest(self):
        if self.balance <= 0:
            print("Insufficient funds.")
            print("Current balance: ", str(self.balance))
        else:
            print("Current balance: ", str(self.balance))
            print("Current interest rate: ", str(self.int_rate))
            self.balance += self.balance * self.int_rate
            print("Balance with interest: ", str(self.balance))

