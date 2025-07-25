from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-270, 270)
        self.levels = 1
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.levels}", align= "left", font= FONT)

    def display_gameover(self):
        self.penup()
        self.goto(0, 0)
        self.write("GameOver!", align="center", font=FONT)

    def increment_levels(self):
        self.levels += 1
