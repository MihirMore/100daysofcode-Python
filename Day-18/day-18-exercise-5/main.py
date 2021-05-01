from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape(name="turtle")

screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
tim.speed(speed=0)
def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
tim.hideturtle()

screen.exitonclick()