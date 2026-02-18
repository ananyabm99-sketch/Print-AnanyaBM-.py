'''class Bank:
    def __init__(self):
        pass
        
    def Create_account(self,name,type_of_account,age,balance =0):
        self.name = name
        self.age = age
        self.type_of_account = type_of_account
        self.__balance = balance
        print("Account Created Successfully\n")

    def Deposit(self,amount):
        self.__balance += amount
        
    def Withdraw(self,withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.withdraw_amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -=self.withdraw_amount
            
    def Check_balance(self):
        print(f"Balance : {self.__balance}")
        
abk = Bank()
abk.Create_account("Ananya","Svg's","17")
abk.Deposit(1000)
abk.Withdraw(100)
abk.Check_balance()
'''

class Account:
    def __init__(self,id,holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0
        
    def check_balance(self):
        print(f"Balance : {self._balance}")
        
    def deposit(self,amount):
        self._balance += amount
        print(f"Deposit Successful.Updated Balance:{self._balance}")
        
    def Withdraw(self,amount):
        if self._balance>=amount:
            self._balance-=amount
            print(f"Withdraw Successful.Updated Balance:{self._balance}")
        else:
            print("Not Enough Funds")
            
            
            
class SavingsAccount(Account):
    def __init__(self,id,holder_name,interest):
        super().__init__(id,holder_name)
        self.interest = interest
        
    def add_interest(self):
        add_interest = self._balance * self.interest
        self._balance += add_interest
        print(f"Interest Added: {add_interest}")
        print(f"Updated Interest : {self._balance}")
        
        
        
class CurrentAccount(Account):
    def __init__(self,id,holder_name):
        super().__init__(id,holder_name)
        
    def Withdraw(self,amount):  #POLYMORPHISM
        OVERDRAFTLIMIT =1000
        if self._balance+OVERDRAFTLIMIT>=amount:
            self._balance-=amount
            print(f"Withdraw Successful.Updated Balance:{self._balance}")
        else:
            print("Not Enough Funds")
            
            
            
class Bank:
    def __init__(self,name,city):
        self.name = name
        self.city = city
        self.__account = {}
        
    def create_account(self,id,holder_name,type,interest=0.0):
        if type=="savings":
            new_account = SavingsAccount(id,holder_name,interest)
        elif type == "current":
            new_account = CurrentAccount(id,holder_name)
        self.__account[id]=new_account
        print("Account creation Successful")
        return new_account
    
    def get_account(self,id):
        if id not in self.__account:
            print("\n ID not found\n")
            return None
        else:
            account = self.__account[id]
            print(f"\nID: {account.id}\nHolder name :{account.holder_name}")
            return account
        
        
        
abk = Bank("ABK","H D Kote")
A1 = abk.create_account("123","Ananya","savings",0.4)
A1.deposit(100)
A1.add_interest()
A1.Withdraw(20)

A2 = abk.create_account("1234","Anvith","current")
A2.deposit(10)
A2.Withdraw(20)