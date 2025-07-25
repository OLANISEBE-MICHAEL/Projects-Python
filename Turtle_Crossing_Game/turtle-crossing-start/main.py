import time
from turtle import Screen
from player import Player
from car_manager import CarManager, STARTING_MOVE_DISTANCE
import random
from scoreboard import Scoreboard

# setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# creating objects from necessary classes
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# listening for key events to move the turtle
screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_car()

    # checking if turtle collides with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.display_gameover()
    # detects if the turtle meets the final destination
        elif player.position()[1] == player.finish_line:
            player.player_reset()
            car_manager.car_reset()
            scoreboard.increment_levels()
            scoreboard.display_level()
    screen.update()
screen.exitonclick()