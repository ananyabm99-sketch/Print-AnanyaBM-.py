'''
turtle = Turtle()
turtle.shape("square")
turtle.color("white")
turtle.shapesize(5,1,0)
turtle.penup()
turtle.goto(360,0)

def go_up():
    new_y = turtle.ycor()+20
    turtle.goto(turtle.xcor(),new_y)
def go_down():
    new_y = turtle.ycor()-20
    turtle.goto(turtle.xcor(),new_y)

screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")
'''