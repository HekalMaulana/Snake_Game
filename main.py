import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Score

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Welcome to my SNAKE GAME")

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.15)

    snake.move()

    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend()
        score.add_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 1:
            is_game_on = False
            score.game_over()

screen.exitonclick()
