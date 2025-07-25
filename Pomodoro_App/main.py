import tkinter as tk
from tkinter import Canvas

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """this resets the whole time when the user clicks on the reset button"""
    global timer, reps   # to be able to access these external variables in this function
    window.after_cancel(timer)  # stop the timer
    canvas.itemconfig(timer_text, text= "00:00")    # reset the timer
    check_label.config(text= "")   # reset checks
    timer_label.config(text= "Timer")  # reset the label
    reps = 0 # reset reps


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """this starts the time for work, short-break and long-break"""
    global reps # to be able access this external variable in this function
    reps += 1
    count_type = 0
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0: # odd number -> time to work
        timer_label.config(text= "Work", fg= GREEN)
        count_type = work_sec
    elif reps % 8 == 0: # time for long break
        timer_label.config(text="Long-Break", fg= RED)
        count_type = long_break_sec
    else:
        timer_label.config(text="Short-Break", fg= PINK)
        count_type = short_break_sec
    count_down(count_type)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global checks, timer
    count_min = count // 60
    count_sec = count % 60

    # ensuring that the second displays :00 or 09 and so on
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    display_time = f"{count_min}:{count_sec}" # the time that would be displayed on the screen
    canvas.itemconfig(timer_text, text= display_time) # canvas.itemconfig() works just like label.config()
    if count > 0:
       timer = window.after(1000, count_down, count - 1) # recurssion
    else:
        start_timer()
        if reps % 2 == 0:
            checks += "✔️"
            check_label.config(text= checks) # to display checks on the screen when the user has done some work

# ---------------------------- UI SETUP ------------------------------- #
# creating the window
window = tk.Tk()
window.title("Pomodoro app")
window.config(padx= 100, pady= 50, bg= YELLOW)


# canvas is a rectangular area in the window which is mainly used when drawing images or complex layout
canvas = Canvas(width= 200, height= 224, bg= YELLOW, highlightthickness= 0)

# this takes the file where the image is located and reads it. it is helpful when using canvas.create_image()
tomato_img = tk.PhotoImage(file= "tomato.png")

# create_image() used when you want to add image as the background
canvas.create_image(100, 112, image= tomato_img )
timer_text = canvas.create_text(100, 130, text= "00:00", fill= "white", font= (FONT_NAME, 35, "bold"))
canvas.grid(row= 1, column= 1)


# creating labels
timer_label = tk.Label(text= "Timer", fg= GREEN, bg= YELLOW, font= (FONT_NAME, 25, "bold"))
check_label = tk.Label(fg= GREEN, bg= YELLOW, font= (FONT_NAME, 15))

timer_label.grid(row= 0, column= 1)
check_label.grid(row= 3, column= 1)


# creating the buttons
start_button = tk.Button(text= "Start", command= start_timer )
reset_button = tk.Button(text= "Reset", command= reset_timer)

start_button.grid(row= 2, column= 0)
reset_button.grid(row= 2, column= 2)
















window.mainloop()