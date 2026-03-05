from turtle import Turtle
class Ball(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1,1,0)
        self.penup()
        self.goto(x_cor,y_cor)
        self.x_cor =10
        self.y_cor =10
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_cor *= -1
    def bounce_x(self):
        self.x_cor *= -1
        self.move_speed *= 0.9
    def reset_position_p1(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1
    def reset_position_p2(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1