from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.big_food = None
        self.big_or_small()


    def big_or_small(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            self.make_big_food()
        else:
            self.make_small_food()


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


    def make_big_food(self):
        self.shapesize(stretch_len= 2, stretch_wid= 2)
        self.color("red")
        self.speed(0)
        self.big_food = True


    def make_small_food(self):
        # self.shapesize() is used to set the size of the turtle it takes in the length and width of the new turtle
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.big_food = None
