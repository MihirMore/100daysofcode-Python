from turtle import Turtle

class Midline(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5,0.5)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,300)
        self.pendown()
        self.goto(0,-300)