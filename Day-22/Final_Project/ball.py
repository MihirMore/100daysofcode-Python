from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.7, 0.7)
        self.penup()
        

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 8
        self.goto(new_x, new_y)    