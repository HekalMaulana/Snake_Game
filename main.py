import time
from turtle import Screen

from snake import Snake

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Welcome to my SNAKE GAME")

snake = Snake(shape="square", color="white")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.segments[0].xcor() > 280:
        is_game_on = False

screen.exitonclick()
