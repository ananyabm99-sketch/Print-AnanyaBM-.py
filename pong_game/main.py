from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle(360,0)
left_paddle = Paddle(-360,0)
ball_go = Ball(0,0)
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")

screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")

game_is_on = True
while game_is_on == True:
    time.sleep(ball_go.move_speed)
    screen.update()
    ball_go.move()
    
    if ball_go.ycor() >=290 or ball_go.ycor() <= -290:
        ball_go.bounce_y()
    if ball_go.distance(right_paddle)<50 and ball_go.xcor()>320 or ball_go.distance(left_paddle)<=50 and ball_go.xcor()<-320:
        ball_go.bounce_x()
    if ball_go.xcor()>380: 
        ball_go.reset_position_p1()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
    if ball_go.xcor()<-380: 
        ball_go.reset_position_p2()
        scoreboard.r_point()
        scoreboard.update_scoreboard()


screen.exitonclick()