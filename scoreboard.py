from turtle import Turtle

ALIGMENT = 'center'
FONT = ("Courier", 22, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.content = None
        self.score = 0
        self.color("white")
        self.hideturtle()
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
