from turtle import Screen
import random
from car_manager import CarManager

screen = Screen()
screen.setup(width= 600, height= 600)

car = CarManager()
car.goto(0, -280)
car.forward(5)





screen.exitonclick()