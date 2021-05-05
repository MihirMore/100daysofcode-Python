from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.04)
    screen.update()
    ball.move()

    # Detect collision with walls 
    if ball.ycor() > 286 or ball.ycor() < -286:
    # Ball will bounce and change direction
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor()> 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()
    
    # Detect if the ball goes beyond the screen and if does reset the game and start going to the opposite side.
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.reset_position()
        ball.bounce_x()
        
        


screen.exitonclick()
