import time
from turtle import Screen

from snake import Snake

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Welcome to my SNAKE GAME")

snake = Snake(shape="square", color="white")

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        screen.bye()
        print("You hit the wall")

# screen.exitonclick()
