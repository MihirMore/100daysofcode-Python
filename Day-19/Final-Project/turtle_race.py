from turtle import Turtle, Screen
import random

is_race_on  = False
screen = Screen()
screen.setup(width=600, height=500)
colors = ["red", "orange", "gold","green","blue", "purple"]
all_turtles = []
screen.title("Turtle Race")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle is going to win the race? Enter a colour: ")
print(user_bet)

y_point = -160

for item in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[item])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=y_point)
    new_turtle.pendown()
    all_turtles.append(new_turtle)
    y_point += 60

print(all_turtles)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 280:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning turtle is {winning_color}.")
                turtle.goto(-150, 100)
                turtle.write(f"You have won! The winner is {winning_color}", align="left", move=False, font=("Calibri", 16, "bold"))
            else:
                print(f"You've lost! The winning turtle is {winning_color}.") 
                turtle.goto(-150, 100)
                turtle.write(f"You have lost. The winner is {winning_color}", align="left",  move=False, font=("Calibri", 16, "bold"))   

    for turtle in all_turtles:
        random_distance = random.randint(1, 10)
        turtle.penup()
        turtle.forward(random_distance)



screen.exitonclick()