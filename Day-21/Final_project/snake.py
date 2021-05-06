from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SHAPE = ((-10, -10), (-10, 10), (0, 20), (10, 10), (10, -10))

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def snake_head(self):
        snake_head_diamond = Screen()
        snake_head_diamond.register_shape("diamond", SHAPE)
        self.segments[0].shape("diamond")
            

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)            
        self.snake_head()

    def add_segment(self, position):        
        new_snake = Turtle(shape="square")
        if len(self.segments) % 2 == 0:
            new_snake.color("darkolivegreen")
        else:    
            new_snake.color("darkseagreen")
        new_snake.penup()
        new_snake.goto(position)
        self.segments.append(new_snake)

    def extend(self):
        # Add a new segment to the snake everytime it hits food
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(2500,2500)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    
    def down(self): 
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)               