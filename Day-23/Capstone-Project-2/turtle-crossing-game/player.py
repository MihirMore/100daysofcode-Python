from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()        
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.color("lawngreen")

    def turtle_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):        
        self.goto(STARTING_POSITION)
        
    def is_player_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            False    
