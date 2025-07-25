from turtle import Turtle, Screen
import random


screen = Screen()

# screen.setup() helps to set the dimensions of the screen rather than getting the default
screen.setup(width= 500,  height= 400)
is_race_on = False

# screen.textinput() is used to show a dialog box that would accept input from the user
user_bet = screen.textinput(title= "Make your bet",  prompt= "Who would win the race? Enter a color: ")
colors = ["red", "orange", "green", "blue", "yellow", "purple"]
list_of_turtles = []

# creating multiple instances of turtles
counter = 0
x_position = -230
y_position = -80
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x_position, y_position)
    list_of_turtles.append(new_turtle)
    y_position += 30

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in list_of_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print("You won!")
            else:
                print(f"You lost! {winning_turtle} won the race")
                
            is_race_on = False
            break













screen.exitonclick()