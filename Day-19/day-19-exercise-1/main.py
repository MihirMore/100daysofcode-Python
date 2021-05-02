from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
screen = Screen()

def move_forward():
    tim.forward(20)

def move_back():
    tim.backward(20)

def move_left():
    new_heading = tim.heading() + 15
    tim.setheading(new_heading)

def move_right():
    new_heading = tim.heading() - 15
    tim.setheading(new_heading)

def clear_screen():
    tim.clear()
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()