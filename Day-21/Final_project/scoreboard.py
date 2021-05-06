from turtle  import Turtle
ALIGNMENT = "center"
FONT = ("Comic Sans MS", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0

        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} \t High Score: {self.highscore}", align = ALIGNMENT, font = FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0  
        self.update_scoreboard()  

    # def game_over(self):
    #     self.goto(0 , 0)
    #     self.write("Game Over", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1        
        self.update_scoreboard()
