from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.color("salmon")
        self.penup()
        self.goto(-315,290)
        self.pendown()
        self.pensize(10)
        self.goto(-315,-277)
        self.goto(310,-277)
        self.goto(310,290)
        self.goto(-315,290)
        self.hideturtle()