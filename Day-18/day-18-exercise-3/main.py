from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape(name="turtle")

screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    color = (r, g, b)
    return color

directions = [0, 90, 180, 270]
tim.pensize(width=6)
tim.speed(speed=6)

for _ in range(200):  
    tim.color(random_color())      
    tim.setheading(random.choice(directions))
    tim.forward(20)


screen.exitonclick()