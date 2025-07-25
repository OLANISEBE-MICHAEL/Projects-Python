from turtle import Turtle, Screen
import random
import turtle

color_list = [(152, 67, 93), (39, 114, 157), (155, 81, 53), (32, 138, 88), (113, 181, 201), (237, 220, 68), (227, 138, 91),
              (223, 79, 46), (220, 115, 132), (203, 72, 99), (40, 58, 108), (122, 193, 179), (92, 167, 63), (111, 39, 57),
              (63, 45, 56), (240, 149, 154), (250, 219, 1), (28, 157, 183), (235, 160, 156), (162, 209, 191), (158, 206, 214),
              (33, 50, 85), (160, 131, 79), (92, 129, 170), (101, 51, 43), (183, 186, 209), (0, 123, 120), (54, 46, 44),
              (10, 92, 114)]
# set color mode
turtle.colormode(255)
tim = Turtle()
screen = Screen()
tim.hideturtle()

tim.shape("turtle")
tim.color("green")

x_position = -200
y_position = -300

# changing position
def change_position(x, y):
    tim.penup()
    tim.goto(x, y)


tim.speed(0)

for y in range(10):
    change_position(x_position, y_position)
    for x in range(10):
        tim.dot(15, random.choice(color_list))
        tim.penup()
        tim.forward(50)
    y_position += 50


screen.exitonclick()