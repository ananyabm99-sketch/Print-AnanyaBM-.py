from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Turtle Race",prompt="Which turtle will win the race?Enter a color:")
print(user_bet)
color = ["red","blue","green","yellow","orange","purple"]
Y_pos = [-70,-40,-10,20,50,80]
all_turtles = []
random_distance = [20,30,40,50,60,70]

for turtle_index in range(0,6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=Y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    
    for t in all_turtles:
        if t.xcor()>230:
            is_race_on = False
            winning_color = t.pencolor() #turtle.pencolor()  #turtle.color() returns a tuple of (pencolor, fillcolor)
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        t.forward(random_distance)
            
        


'''tim.speed("fastest")
def move_forward():
    
    tim.forward(100)
def move_backward():
    tim.backward(100)
def turn_left():
    tim.left(10)
def turn_right():
    new_heading = tim.heading()-10
    tim.setheading(new_heading)
def turn_curve():
    tim.circle(30,30)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkey(key = "M",fun = move_forward) #func_1 and func_2 = func_1(func_2)
screen.onkey(key = "B",fun = move_backward)
screen.onkey(key = "L",fun = turn_left)
screen.onkey(key = "R",fun = turn_right)
screen.onkey(key = "C",fun = turn_curve)
screen.onkey(key = "E",fun = clear_screen)
'''
screen.exitonclick()