from turtle import Turtle, Screen
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
screen = Screen()

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.finish_line = FINISH_LINE_Y
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def player_reset(self):
        screen.tracer(0)
        self.goto(STARTING_POSITION)
        screen.update()




