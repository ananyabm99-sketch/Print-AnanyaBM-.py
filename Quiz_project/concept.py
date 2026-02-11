'''
#"____________________________________CONCEPT________________________________________"     

class User:    #pascal case -- class 1st letter capital
    pass
    
    
user_1 = User()    #object
user_1.id = "22930"
user_1.name = "Ananya"
user_1.fathers_name = "Mahadev"    #attributes
print(user_1.fathers_name)

user_2 = User()
user_2.id  = "1233"
user_2.name = "Pavithra"
user_2.fathers_name = "Manju"
print(user_2.fathers_name)

#constuctor --  def__init__(self):
#                  initialise attribute()

class Car:
    def __init__(self,seats):    #inside parenthesis parameters
        self.seats = seats    #attribute
my_car = Car(5)   #or my_car.seats = 5(both are same)



class User:
    def __init__(self,user_id,user_name):
        self.id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0
    def follow(self,user):
        user.followers +=1
        self.following +=1

user1 = User("000","Ananya") 
print(user1.user_name)
print(user1.followers)
user2 = User("111","Anvith")
print(user2.id)   

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
'''

