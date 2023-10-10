from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)
    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1

    def reset(self):
        self.goto(0, 0)
        self.move_speed *= 0.9
        self.move_x *= -1

    def ball_move(self):
        self.xcor() * 2
        self.ycor() * 2






