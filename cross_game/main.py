import time
from turtle import Turtle,Screen
from player import Player
from car_manager import CarManager   
from scoreboard import Score
screen = Screen()
screen.setup(600,600)
screen.bgcolor("White")
screen.tracer(0)

play = Player()
play.move()
score = Score()
car_manager = CarManager()


screen.listen()
screen.onkey(play.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()
    for car in car_manager.all_cars:
        if car.distance(play)<20:
            game_is_on = False
            score.Final_score()
    if play.is_at_finish_line():
        play.go_to_start()
        car_manager.level_up()
        score.update_score()

    
    
screen.exitonclick()    

