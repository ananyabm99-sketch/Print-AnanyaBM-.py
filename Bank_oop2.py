class Bank:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.__balance:
            self.__balance -= withdraw_amount
            print(f"Withdrawn: {withdraw_amount}")
        else:
            print("No enough funds")

    def display_balance(self):
        print(f"Balance : {self.__balance}")


# Object
c1 = Bank("Ananya", 1000000)
c1.deposit(100000)
c1.withdraw(300000)
c1.display_balance()