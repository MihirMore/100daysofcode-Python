from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=500)
colors = ["red", "orange", "gold","green","blue", "purple"]

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle is going to win the race? Enter a colour: ")
print(user_bet)

y_point = -160

for item in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[item])
    tim.penup()
    tim.goto(x=-280, y=y_point)
    tim.pendown()
    y_point += 60



screen.exitonclick()