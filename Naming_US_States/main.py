from turtle import Turtle, Screen
import pandas as pd

# parameter definintion for the turtle.write()
ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")

# creating the screen and using the blank map as the background of the screen
screen = Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"

# reading the data into a pandas dataframe
file_name = "50_states.csv"
data = pd.read_csv(file_name)
all_states = data["state"].to_list()
guessed_state = []


# is used to add a shape that can later be used by the turtle.shape()
screen.addshape(image)

# creating a background turtle object for the background
background = Turtle()
background.shape(image)
is_game_on = True


# functions that would help perform main tasks
def retrieve_state(state):
    """retrieves the coordinates of the guessed state from the csv file"""
    name_of_state = data[data["state"] == state]
    coordinates = (int(name_of_state.iloc[0]['x']), int(name_of_state.iloc[0]['y']))
    return coordinates

def move_state(state, coordinates):
    """moves the state to the appropriate position per user guess"""
    # creating a turtle object for writing the states on the screen
    writer = Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(coordinates)
    writer.write(f"{state}", align=ALIGNMENT, font=FONT)

def store_unguessed_states():
    """stores all the states the users did not guess in a csv file"""
    unguessed_state = [state for state in all_states if state not in guessed_state]
    df = pd.DataFrame(unguessed_state)
    df.to_csv("remaining_states.csv")


while is_game_on:
    # asking user for input
    user_answer = screen.textinput(f"{len(guessed_state)}/50 states correct", prompt= "Enter a state").title()

    # going out of the game using the exit word
    if user_answer == "Exit":
        store_unguessed_states()
        break
    if user_answer in all_states:
        # ensuring no errors when a user guesses a state user had already guessed before
        if not user_answer in guessed_state:
            state_coordinate = retrieve_state(user_answer)
            move_state(user_answer, state_coordinate)
            guessed_state.append(user_answer)

        if len(guessed_state) == 50:
            # Game has ended
            is_game_on = False

screen.exitonclick()


