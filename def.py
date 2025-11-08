class Database:
    def __init__(self):
        self.storage = {}
    def write(self,key,value):
        self.storage[key]  = value
        
    def read(self,key):
        return self.storage[key]    
db = Database()        
db.write("Ananya","17")
print(db.storage)

class ATM:
    def __init__(self,balance):
        self.__balance = balance       #private attribute
    def deposit(self,amount) :
        self.__balance += amount
        print(f"Deposited : {amount}.\n balance : {self.__balance}")
    def withdraw(self,amount) :
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw : {amount}. \n New balance : {self.__balance}")  
            
        else:
            print("Insufficient balance")  

atm = ATM(100)             
atm.deposit(50)
atm.withdraw(25)


class user:
    def __init__(self,username,password):
        self.username =username
        self.password = password
    def get_username(self):
        return self.username 
    def check_password(self, password):
        return password == self.password
user = user("dev_arya","DG209")   
print(user.get_username())    
print(user.check_password(123))      
print(user.check_password("DG209"))

    
    
class Car:
    def start_engine(self):
        print("Engine started")

    def accelerate(self):
        print("Car accelerating")

    def brake(self):
        print("Car stopping")

car = Car()
car.start_engine()  # Abstracts complex internal workings
car.accelerate()
car.brake()        




        