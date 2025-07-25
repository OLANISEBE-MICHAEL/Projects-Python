from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("green")


def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_anti_clockwise():
    tim.left(10)

def move_clock_wise():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()


# we use the onkey() to specify the key for the event listener
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_clock_wise, "d")
screen.onkey(move_anti_clockwise, "a")
screen.onkey(clear_screen, "c")

# to listen for events we have to make use of the .listen() method which takes in 2 arguments
# the function and the key that would trigger it
screen.listen()
screen.exitonclick()