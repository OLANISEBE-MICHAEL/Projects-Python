from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score
import time

screen = Screen()
screen.setup(width= 600, height= 600)

# screen.bgcolor() is used to set the background of the screen
screen.bgcolor("black")
screen.title("My snake game")

# setting screen.tracer(0) tells python to stop refreshing the screen after every turtle movements
screen.tracer(0)

# creating necessary objects
snake = Snake()
food = Food()
score = Score()

# screen.listen() is used to listen for key events
screen.listen()

# screen.onkey() is used to specify the key that would perform a specific function
screen.onkey(snake.face_up, "Up")
screen.onkey(snake.face_down, "Down")
screen.onkey(snake.face_right, "Right")
screen.onkey(snake.face_left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    # moving the snake
    snake.move()

    # detecting collision with the food
    print(food.big_food)
    if snake.head.distance(food) < 15 :
        if food.big_food:
            score.increment(2)
            snake.extend_segments(2)
        else:
            score.increment(1)
            snake.extend_segments(1)

        food.refresh()

    # detecting collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    # detecting snake collision with tail
    for segment in snake.segments[1: ]:
        if snake.head.distance(segment) < 10 :
            score.reset()
            snake.reset()

screen.exitonclick()
