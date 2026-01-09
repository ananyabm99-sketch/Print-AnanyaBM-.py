class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self) :
        print(f"My name is {self.name} and I am {self.age} years old.")
person1 = person("Ananya",17) 
person1.introduce() 

class Laptop:
    def __init__(self,brand,price)    :
        self.brand = brand
        self.price = price
    def show_info(self):
        print(f"Laptop Brand : {self.brand},price: {self.price}") 
laptop1 = Laptop("Dell",60000)
laptop2= Laptop("hp",71000)   
laptop1.show_info()
laptop2.show_info()   

class Book:
    def __init__(self,title,author= "unknown"):
        self.title = title
        self.author = author
    def show_book(self)    :
        print(f"Title : {self.title}\nAuthor : {self.author}")
book1 = Book("Python Programming")  
book2 = Book("Machine Learning","Andrew Ng")      
book1.show_book()
book2.show_book()
