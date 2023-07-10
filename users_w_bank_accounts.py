class BankAccount:
    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    @classmethod
    def print_accounts(cls):
        for account in cls.accounts:
            print("Account Info:")
            print("  Interest Rate:", account.int_rate)
            print("  Balance:", account.balance)
            print("................")

    def deposit(self, amount):
        print("Deposit: ", amount)
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds.")
            print("Current balance:", self.balance)
        else:
            print("Withdrawal: ", amount)
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print("Current balance:", self.balance)
        return self

    def yield_interest(self):
        if self.balance <= 0:
            print("Insufficient funds.")
            print("Current balance: ", self.balance)
        else:
            self.balance += self.balance * self.int_rate
            print("Balance with interest: ", self.balance)
        return self
    
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self



user1 = BankAccount(1.05, 1000000)
user2 = BankAccount(1.10, 42000)
user3 = BankAccount(1.02, 10000)

user1.display_account_info().deposit(1000000).deposit(1000000).deposit(1000000).withdraw(1).yield_interest().display_account_info()
user2.display_account_info().deposit(20).deposit(20).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

BankAccount.print_accounts()