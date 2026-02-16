'''class car:
    def __init__(self,car_id,name,year,price_per_day,rented_days=0,status ="Available"):
        self.car_id = car_id
        self.name = name
        self.price_per_day = price_per_day
        self.status = status
        self.rented_days = rented_days
        self.year = year
        self.rented_days = rented_days
    def display_details(self):
        print(f"Name : {self.name}\nCar ID : {self.car_id}\nRent per day: {self.price_per_day}\nStatus :{self.status}\nRented Days:{self.rented_days}\n")
    
    def update_status(self,new_status):
        self.status = new_status
        print(f"Car :{self.car_id} updated to {self.status}")
    def calculate_rental_price(self):
        total_price = self.price_per_day + self.rented_days
        print(f"Total price for {self.name} : {total_price}")
c1 = car("123","Toyota","2019",1200,30)
c1.display_details()

#1>
class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def display_info(self):
        print(f"Car Brand : {self.brand}\nModel :{self.model}")
my_car = car("Toyota","corolla")
my_car.display_info()

#2>
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello ,my name is {self.name} and my age is {self.age}\n")
person1 = Person("Ananya",17)
person1.greet()
person2 = Person("Anvith",12)
person2.greet()

#3>
class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} is Barking!")
        
dog1 = Dog("Gappu","Beagle")       
dog2 = Dog("Rex","Labrader Ratriver")
dog1.bark()
print(dog1.breed)
dog2.bark()
print(dog2.breed)

#4>. Encapsulation 
class ATM:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
        print(f"Deposited {amount}\nNew Balance {self.__balance}")
    def withdraw(self,amount):
        if amount<= self.__balance:
            self.__balance -= amount
            print(f"Withdrew : {amount}\nNew balance : {self.__balance}")
        else:
            print("Insufficient Balance\n")
atm = ATM(10000)
atm.deposit(1000)
atm.withdraw(12000)

#5>.
class User:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
    def get_username(self):
        return self.username
    def check_password(self,password):
        return password == self.__password
er = User("Ananya","4678")
print(er.get_username())
print(er.check_password("Bhagya123"))
print(er.check_password("4678"))

#6>.Abstraction
class Car:
    def start_ingine(self):
        print("Engine starting")
    def accelerate(self):
        print("Car accelerating")
    def brake(self):
        print("car stopping")
car = Car()
car.start_ingine()
car.accelerate()
car.brake()

class Database:
    def __init__(self):
        self.__storage = {}
    def save_data(self,key,value):
        self.__storage[key]= value
        print(f"Data saved for {key}")
    def get_data(self,key):
        return self.__storage.get(key,"No data found")      #get returns the value if existed
db = Database()
db.save_data("user_101",{"name":"Ananya","age":17})
print(db.get_data("user_101"))


class Family:
    def __init__(self,surname):
        self.surname = surname
class Child(Family):
    def __init__(self,surname,name):
        super().__init__(surname)
        self.name = name
child = Child("Gowda","Anvith")
print(f"{child.name} {child.surname}")

class User:
    def __init__(self,username):
        self.username = username
    def login(self):
        print(f"{self.username} logged in")
class Admin(User):
    def delete_user(self,user):
        print(f"Admin {self.username} delete the user {user}")
admin = Admin("Ananya B M")
admin.login()
admin.delete_user("user_102")

class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Bark")
class Cat(Animal):
    def make_sound(self):
        print("meow")
animals = [Dog(),Cat()]
for animal in animals:
    animal.make_sound()

class Notification:
    def send(self):
        pass
class EmailNotification(Notification):
    def send(self):
        print("Sending Email")
class SMSNotification(Notification):
    def send(self):
        print("SMS sending")
notification=[EmailNotification(),SMSNotification()]
for noti in notification:
    noti.send()
'''