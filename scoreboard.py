from turtle import Turtle

ALIGMENT = 'center'
FONT = ("Courier", 22, "normal")


def change_data_file(new_data):
    with open("data.txt", "w") as file:
        file.write(new_data)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.content = None
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.read_file()
        self.high_score = self.content
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def read_file(self):
        with open("data.txt", "r") as file:
            self.content = int(file.read())

    def reset(self):
        self.read_file()
        if self.score > self.high_score:
            self.high_score = self.score
            change_data_file(str(self.high_score))
        self.score = 0
        self.update_score()
