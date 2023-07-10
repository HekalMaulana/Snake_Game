from turtle import Turtle

ALIGMENT = 'center'
FONT = ("Courier", 22, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.highscore = 0
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", align=ALIGMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()


