from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("khaki2")
        self.penup()
        self.hideturtle()
        self.current_level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200, 240)        
        self.current_level += 1
        self.write(f"Level {self.current_level}", align="center", font=FONT)   
        
    def game_over(self):
        game_message = Turtle()
        game_message.hideturtle()
        game_message.color("lemonchiffon2")
        game_message.write("Game Over", align="center", font=FONT)    