from turtle import Turtle, Screen

tim = Turtle()
tim.shape(name="turtle")
tim.color("tomato3")
# for _ in range(4):
#     tim.forward(150)
#     tim.right(90)

tim.pensize(width=3)
for _ in range(20):
    tim.pendown()
    tim.forward(8)
    tim.penup()
    tim.forward(8)

screen = Screen()
screen.exitonclick()