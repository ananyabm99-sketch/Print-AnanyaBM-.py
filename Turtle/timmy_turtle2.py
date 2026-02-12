
'''from turtle import Turtle, Screen
import random
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("purple")


timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)

timmy_the_turtle.forward(100)

timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)

for i in range(20):
    timmy_the_turtle.right(60)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(30)
    for j in range(30):
        timmy_the_turtle.forward(50)
        timmy_the_turtle.right(60)
screen = Screen()
screen.exitonclick()

#from turtle import *   #import everything
#import turtle as t  #import turtle and give it an alias
#tom = t.Turtle() #create a turtle named tom
import heroes
print(heroes.gen())


'''

from turtle import Turtle,Screen
import random


screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.pensize(12.3)
tim.speed("fastest")

movee = [90,180,270,360]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

for _ in range(200):
    tim.color(random_color())
    tim.forward(30) 
    tim.setheading(random.choice(movee))
screen.screensize(width = 500,height =500)
screen.exitonclick()

