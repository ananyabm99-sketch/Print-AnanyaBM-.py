#Getters ,Setters,Method overloading and overriding
class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def get_name(self) :
        return self.__name
    def set_name(self,name) :
        self.__name = name
           
s = Student("Ananya",22)   
print(s.get_name())   
s.set_name("Vinith")
print(s.get_name())
print("_"*42)

class fingers:
    def __init__(self,name,height):
        self.__name = name
        self.__height = height
    def get_name(self) :
        return self.__name
    def set_height(self,height):
        if isinstance (height,float) :
            self.__height = height
        else:
            print("height should be a float")
    def get_height(self) :
        return self.__height           
x = fingers("Thumb",4)
print(x.get_name())
x.set_height(4.5)
print(x.get_height())
print("_"*42)

#Method Overloading:
class calculator:
    def add (self,a,b,c=0):
        print(a+b+c)
c = calculator()        
c.add(1,2)
c.add(1,2,3)
print("_"*42)

#Method Overriding:
class Animal:
    def make_sound(self):
        print("Animal is making sound")
class Dog(Animal):
    def make_sound(self):
        print("Bark")
d = Dog()        
d.make_sound()
print("_"*42)

#Abstract class
from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Bike(vehicle):
    def __init__(self,name):
        self.name = name
    def start_engine(self) :
        print("Starting engine")    
b = Bike("Royal Emfield")
print(b.name)
print("_"*42)

from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod    
    def perimeter(self):
        pass
class Circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius *self.radius
    def perimeter(self) :
        return 2*3.14*self.radius
x = Circle(6)  
print("Area: ",x.area() )     
print("Perimeter: ",x.perimeter() )                    
print("_"*42)                       
    