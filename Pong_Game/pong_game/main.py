from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("My Pong Game")
# screen.setup() is used to create the width and height of the screen
screen.setup(width= 800, height=600)
screen.tracer(0)

# creating paddle objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBoard()

# listening for keyboard events for both paddles
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_score)
    ball.move()

    # checking if the ball hits the top and down walls
    if ball.ycor() >= 280 or ball.ycor() < -280:
        ball.y_bounce()

    # checking if the ball hits the paddle
    if ball.distance(r_paddle) <= 50 and ball.xcor() > 320:
        ball.x_bounce()
    elif ball.distance(l_paddle) <= 50 and ball.xcor() < -320:
        ball.x_bounce()



    # checking if the ball is out of bounds
    # if r_side misses
    if ball.xcor() > 380:
        ball.right_reset()
        score_board.l_point()

    # if l_side misses
    if ball.xcor() < -380:
        ball.left_reset()
        score_board.r_point()


    screen.update()
screen.exitonclick()