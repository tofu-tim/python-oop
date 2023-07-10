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
        self.accounts = []

    def add_account(self, int_rate, balance):
        account = BankAccount(int_rate, balance)
        self.accounts.append(account)

    def transfer_money(self, amount, other_user, sender_index, recipient_index):
        from_account = self.accounts[sender_index]
        to_account = other_user.accounts[recipient_index]

        if from_account.balance >= amount:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print("Transfer complete.")
        else:
            print("Insufficient funds for transfer.")   

    def make_withdrawal(self, account_index, amount):
        account = self.accounts[account_index]
        account.withdraw(amount)
        return self
    
    def display_user_balance(self, account_index):
        account = self.accounts[account_index]
        print(self.name)
        account.display_account_info()
    
    def make_deposit(self, account_index, amount):
        account = self.accounts[account_index]
        account.deposit(amount)
        return self
    
user1 = User("Diego Najera", "dnajera@primitiveskate.com")
user2 = User("Felipe Mota", "felipe.mota@primitiveskate.com")

# add_account test
user1.add_account(0.02, 10000)
user1.display_user_balance(0)

user2.add_account(0.04, 2000)
user2.display_user_balance(0)