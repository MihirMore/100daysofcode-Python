from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape(name="turtle")
timmy_the_turtle.color("tomato3")
for _ in range(4):
    timmy_the_turtle.forward(150)
    timmy_the_turtle.right(90)

screen = Screen()
screen.exitonclick()