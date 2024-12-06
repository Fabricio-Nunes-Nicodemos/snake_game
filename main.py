from turtle import Screen
from src.snake import Snake
from src.food import Food
from src.scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(snake.move_speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 6:
        food.refresh()
        snake.extend()
        scoreboard.increse_score()

    # Detect collision with wall
    if snake.head.xcor() > 385 or snake.head.xcor() < -385 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
