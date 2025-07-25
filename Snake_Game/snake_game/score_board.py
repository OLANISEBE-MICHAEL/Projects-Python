from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 16, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.high_score = None
        # we use the open() function and the "with" keyword to perform file handling operations
        with open("data.txt") as score_data:
            self.high_score = int(score_data.read())

        self.penup()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} | High Score : {self.high_score}", align= ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode= "w") as score_data:
                score_data.write(str(self.high_score))

        self.score = 0
        self.update_score()

    def increment(self, point):
        self.score += point
        self.update_score()






