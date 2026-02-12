'''from turtle import Turtle,Screen
#import turtle
tim = Turtle()
for i in range (10):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)
screen = Screen()
screen.exitonclick()
'''
from turtle import Turtle,Screen  
import random       
tim = Turtle()
colours = ["aquamarine2","blue2","coral2","cyan2","DarkOrchid2","DarkSeaGreen2","DeepPink2","DeepSkyBlue2","FireBrick2","Gold2"]
def draw_shapes(num_sides):
    angle = 360/num_sides               #360/no of sides

    for _ in range(num_sides):
        
        tim.forward(100)
        tim.right(angle)
for shape_sides in range(3,11):
    tim.color(random.choice(colours))
    draw_shapes(shape_sides)
screen = Screen()
screen.exitonclick()        
    
