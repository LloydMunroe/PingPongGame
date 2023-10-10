from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scores import Score
import time

screen = Screen()
screen.setup(height=600, width=700)
screen.bgcolor("black")
screen.title("My Ping Pong Game")
screen.tracer(0)

ball = Ball()

r_score = Score((250, 260))
l_score = Score((-250, 260))



r_paddle = Paddle((330, 0))
l_paddle = Paddle((-330, 0))

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up") # use onkeypress to get the ping moving while you press it.
screen.onkeypress(r_paddle.go_down, "Down") # "Up" and 'Down' are the names for the arrow keys on the keyboard

screen.onkeypress(l_paddle.go_up, "a") # onkey is registered with the release of the press,
screen.onkeypress(l_paddle.go_down, "z")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Dectect Collision with Paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 300:
        ball.bounce_x()
        r_score.rec_score()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -300:
        ball.bounce_x()
        l_score.rec_score()

    # Dectect Ball Out of Play
    if ball.xcor() > 350:
         ball.reset()
         ball.ball_move()
         l_score.rec_score()

    if ball.xcor() < -350:
            ball.reset()
            ball.ball_move()
            r_score.rec_score()
            print(r_score.rec_score())

    # if r_score.rec_score() == 10:
    #         l_score.game_over()
    #         r_score.you_win()



screen.exitonclick()









