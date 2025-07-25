import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_FOR_LANG = ("Ariel", 40, "italic")
FONT_FOR_WORD = ("Ariel", 60, "bold")
FONT_FOR_TIMER = ("Ariel", 25, "bold")

#------------------------------------ GETTING THE DATA ----------------------------------------#
# incase the file does not exist
word_list = {} # a list of dictionary obtained from csv file
try:
    word_data = pd.read_csv("./data/words_to_learn")
except FileNotFoundError:
    word_data = pd.read_csv("./data/french_words.csv")
    word_list = word_data.to_dict(orient= "records") # it returns a list of dictionaries
else:
    word_list = word_data.to_dict(orient= "records") # it returns a list of dictionaries

word_pair = {} # created an empty dictionary since as starting value since using it in a function


#------------------------------------ DISPLAY CARDS--------------------------------------------#
def next_card():
    """this displays the card to translate which is french"""
    global word_pair
    word_pair = random.choice(word_list) # gets a random dictionary from the list of dictionaries
    canvas.itemconfig(front_card_display, image=front_image)
    canvas.itemconfig(lang, text= "French", fill= "black")
    canvas.itemconfig(word, text= word_pair["French"], fill= "black")
    right_button.grid_remove() # hide button
    wrong_button.grid_remove() # hides the button
    timer() # reset timer

def flip_card():
    """this flips the card after 3 seconds"""
    canvas.itemconfig(front_card_display, image= back_image)
    canvas.itemconfig(lang, text= "English", fill= "white")
    canvas.itemconfig(word, text= word_pair["English"], fill= "white")
    right_button.grid(row=1, column=0)
    wrong_button.grid(row=1, column=1)

#------------------------------------ TIMER --------------------------------------------#
def timer(count = 3):
    """this controls the timer the user has before the cards get flipped"""
    if count >= 0:
        display = f"TIMER: {count}"
        timer_label.config(text= display)
        window.after(1000, timer, count - 1)
    else:
        flip_card()

def is_known():
    """this removes the word pair from the list since the card is already known"""
    word_list.remove(word_pair)
    data = pd.DataFrame(word_list)
    data.to_csv("./data/words_to_learn", index= False)
    next_card()

#------------------------------------ UI SET UP ----------------------------------------#
# creating window
window = tk.Tk()
window.title("FlashCard App")
window.config(bg= BACKGROUND_COLOR, padx= 50, pady= 50)

# creating canvas
canvas = tk.Canvas(width= 800, height= 526)
front_image = tk.PhotoImage(file= "./images/card_front.png") # creating a reference to the image
back_image = tk.PhotoImage(file= "./images/card_back.png")   # creating a reference to the image
canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
front_card_display = canvas.create_image(400, 263, image= front_image) # creating images

lang = canvas.create_text(400, 150, text= "", font= FONT_FOR_LANG) # creating texts
word = canvas.create_text(400, 263, text= "", font= FONT_FOR_WORD)

timer_label = tk.Label(text="", font=FONT_FOR_TIMER, bg=BACKGROUND_COLOR)
timer_label.grid(row=0, column=3, sticky="n")
canvas.grid(row= 0, column= 0, columnspan= 2)


# creating button
right_image = tk.PhotoImage(file= "./images/right.png")
right_button = tk.Button(image= right_image, bg= BACKGROUND_COLOR, command= is_known, bd= 0)

wrong_image = tk.PhotoImage(file= "./images/wrong.png")
wrong_button = tk.Button(image= wrong_image, bg= BACKGROUND_COLOR, command= next_card, bd= 0)


next_card()
window.mainloop()


