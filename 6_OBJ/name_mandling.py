class Account:
    def __init__(self, _balance):
        self.__balance = _balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New _balance is {self.__balance}")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrew {amount}. New _balance is {self.__balance} ")
        else:
            print("Insufficient funds")
    def show__balance(self):
        print(f"残高は {self.__balance}円です")
myaccount = Account(10000)
myaccount.deposit(5000)
myaccount.withdraw(3000)
myaccount.show__balance()
print(dir(myaccount))
# print(myaccount.__balance) ← これはエラーになる