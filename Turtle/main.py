'''import colorgram
rgb_colors = []
colors = colorgram.extract("image.jpg",20)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)
'''
from turtle import Turtle,Screen
import random
colors_list = [(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62)]
screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")

tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(250)
tim.setheading(0)

for i in range (10):
    for j in range(10):
        tim.dot(20,random.choice(colors_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
        
    tim.setheading(90)
    tim.penup()
    tim.forward(50)
    tim.setheading(180)
    tim.penup()
    tim.forward(500)
    tim.setheading(0)
screen.exitonclick()   
        