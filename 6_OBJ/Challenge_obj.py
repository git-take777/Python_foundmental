class Account
    count = 0
    def __init__(self,balance, account_name):
        self.balance = balance
        self.account_name = account_name
        self.account_number = Account.count + 1
        Account.count += 1
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.account_nuber} {self.account_name} Withdrew {amount}. New balance is {self.balance} ")
        else:
            print("Insufficient funds")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")
