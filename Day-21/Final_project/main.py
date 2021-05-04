from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from border import Border
import time

screen = Screen()
screen.setup(width=650, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
border = Border()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left,"Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)    
    snake.move()

    # Detect collision of snake with food.
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 310 or snake.head.xcor() < -310 or snake.head.ycor() > 290 or snake.head.ycor() < -275:
        game_is_on = False
        scoreboard.game_over() 

    # Detect collision with tail
    # If the head collides with any segemnt of the snake then end the game.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()