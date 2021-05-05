from turtle import Turtle
UP = 90
DOWN = 270

class Paddle(Turtle):
    
    def __init__(self, position, color):
        super().__init__()
        self.penup()        
        self.shape("square")
        self.goto(position)
        self.color(color)
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        

    def up(self):
        new_y = self.ycor() + 30
        self.goto(x = self.xcor(), y = new_y)    

    def down(self):
        new_y = self.ycor() - 30
        self.goto(x = self.xcor(), y = new_y)