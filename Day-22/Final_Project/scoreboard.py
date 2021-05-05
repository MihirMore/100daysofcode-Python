from turtle import Turtle

FONT = ("Comic Sans MS", 60, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.color("dodgerblue")
        self.write(self.l_score, align = "center", font = FONT)
        self.goto(100, 200)
        self.color("chartreuse")
        self.write(self.r_score, align = "center", font = FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()    