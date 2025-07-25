from turtle import Turtle
import random
FINAL_POSITION = (380, 300)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move= 10
        self.move_score = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.move_score *= 0.9
        self.x_move *= -1

    def reverse_direction(self):
        self.x_move *= -1
        self.y_move *= -1

    def right_reset(self):
        self.goto(0, 0)
        self.reverse_direction()

    def left_reset(self):
        self.move_score = 0.1
        self.goto(0, 0)
        self.reverse_direction()

