from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((350,0))
r_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.08)
    screen.update()
    ball.move()



screen.exitonclick()
