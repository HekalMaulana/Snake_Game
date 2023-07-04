from turtle import Turtle,Screen
import time

screen = Screen()

screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to my SNAKE GAME")

snake_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []

is_game_on = True

for cor_position in snake_position:
    new_segment = Turtle(shape="square")
    new_segment.speed("fastest")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(cor_position)
    segments.append(new_segment)

while is_game_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        x_position = segments[seg_num - 1].xcor()
        y_position = segments[seg_num - 1].ycor()
        segments[seg_num].goto(x=x_position, y=y_position)

    segments[0].forward(20)

    if segments[0].xcor() > 280:
        is_game_on = False




screen.exitonclick()