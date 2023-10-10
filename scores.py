from turtle import Turtle
position = (0, 0)
class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("green")
        self.score = 0
        self.one = 1
        self.penup()
        self.goto(position)
        self.write(f"Score:{self.score}", move=False, align="left", font=("arial", 15, "normal"))
        self.hideturtle()


    def rec_score(self):
        self.clear()
        self.score += self.one
        self.write(f"Score:{self.score}", move=False, align="left", font=("arial", 15, "normal"))

    def game_over(self, num):
        if num == 10:
            self.write("Game Over", move=False, align="left", font=("arial", 20, "normal"))

    def you_win(self):
        self.write("You Win", move=False, align="left", font=("arial", 20, "normal"))



