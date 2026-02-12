#flower drawing
'''from turtle import Turtle,Screen, color
import random
screen = Screen()
screen.colormode(255)

tim = Turtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


tim.speed("fastest")
for _ in range(80):
    tim.color(random_color())
    tim.circle(100)
    tim.right(5)

screen.exitonclick()
tim.circle(10)
'''
'''tim.heading()-to get the co-ordinate'''

from turtle import Turtle,Screen, color
import random
screen = Screen()
screen.colormode(255)

tim = Turtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color
tim.speed("fastest")
def draw_splines(space_gap):
    for _ in range(int(360/space_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + space_gap)
draw_splines(5)
screen.exitonclick()
'''tim.heading()-to get the co-ordinate------(0,0)'''
