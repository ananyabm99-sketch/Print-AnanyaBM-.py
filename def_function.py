class database:
    def __init__(self):
        self.__storage = {}
    def save_data(self,key,value):
        self.__storage[key] = value
    def get_data(self,key):
        return self.__storage.get(key) 
db = database()
db.save_data("A",{"name ": "Anu","age": 17})
print(db.get_data("A"))

class family:
    def __init__(self,surname):
        self.surname = surname
class child(family):
    def __init__(self,surname,name):
        super().__init__(surname)
        self.name = name
c = child("Gowda","Anvith") 
print(f"{c. name} {c. surname}")        

class user:
    def __init__(self,username):
        self.username = username
class admin(user):
    def delete_user(self,user):
        self.user = user
        print(f"Admin {self.username} deleted {user}")
        
admin = admin("Ananya")      
admin.delete_user("Anu")

class animal:
    def make_sound(self):
        pass
class hen(animal):
    def make_sound(self):
        print("kokokoooko")        
class cow(animal)   :
    def make_sound(self):
        print("mow")     
class duck(animal)    :
    def make_sound(self):
        print("quak")    
animals = [ hen,cow,duck]        
for animal in animals:
    animal.make_sound()
           
        
          