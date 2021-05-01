from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape(name="turtle")

tim.pensize(width=3)
for _ in range(20):
    tim.pendown()
    tim.forward(8)
    tim.penup()
    tim.forward(8)

screen = Screen()
screen.exitonclick()
