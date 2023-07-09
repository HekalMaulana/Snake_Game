from turtle import Turtle

ALIGMENT = 'center'
FONT = ("Courier", 22, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.score}", align= ALIGMENT, font= FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"Game Over", align=ALIGMENT, font=FONT)
