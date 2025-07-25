import tkinter as tk
from tkinter import Canvas
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', "@", "^", "-", "=", "_", "{", "}", "[", "]", "/", "|", "?", ">",
           "<", ";", ":", "~", ]
file_name = "password_data.json"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """this generates passwords based on the above list"""
    password_entry.delete(0, tk.END)
    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    # random.sample(list, k=) returns a sample from a list without replacement
    letter_combination = "".join(random.sample(letters, k=nr_letters))
    number_combination = "".join(random.sample(numbers, k=nr_numbers))
    symbol_combination = "".join(random.sample(symbols, k=nr_symbols))

    # random.shuffle() is used to randomly shuffle items in an iterable
    generated_password = list(letter_combination + number_combination + symbol_combination)
    random.shuffle(generated_password)

    generated_password = "".join(generated_password)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- UPDATE DETAILS ------------------------------- #
def delete():
    """Deletes the details of a website specified by the user"""
    website_to_delete = website_entry.get().title()
    question = f"Are you sure you want to delete your details associated with {website_to_delete}"
    try:
        with open(file_name) as file:
            data = json.load(file)
            is_delete = messagebox.askyesno(title= f"Delete {website_to_delete}",  message= question)
            if is_delete:
                del data[website_to_delete]
    except FileNotFoundError:
        messagebox.showerror(title="No data", message="You have not added any password")
    except KeyError as error:
        error_msg = f"Sorry, the website {error} does not exist please enter the correct name of the website"
        messagebox.showerror(title= "Invalid Website", message= error_msg)
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        with open(file_name, "w") as new_file:
            json.dump(data, new_file, indent= 4)
            messagebox.showinfo(title= "Successful", message= f"{website_to_delete} details has been deleted✔️")


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search():
    """searches for a given website and login details proviided by the user"""
    website_to_search = website_entry.get().title()
    try:
        with open(file_name) as file:
           data = json.load(file)
           email = data[website_to_search]["email"]
           password = data[website_to_search]["password"]
    except FileNotFoundError:
        messagebox.showerror(title="No data", message="You have not added any password")
    except KeyError as error:
        error_msg = f"Sorry, the website {error} does not exist please enter the correct name of the website"
        messagebox.showerror(title= "Invalid Website", message= error_msg)
        website_entry.delete(0, tk.END)
    else:
        gotten_details = f"Your Email: {email}\nYour Password: {password}"
        messagebox.showinfo(title= website_to_search, message= gotten_details)

# ---------------------------- UPDATE DETAILS ------------------------------- #
def update():
    """updates previously existing details for a given website"""
    website_to_update = website_entry.get().title()
    question = "Are you sure you want to update your details?"
    try:
        with open(file_name) as file:
            data = json.load(file)
            email = data[website_to_update]["email"]
            password = data[website_to_update]["password"]
    except FileNotFoundError:
        messagebox.showerror(title="No data", message="You have not added any password")
    except KeyError as error:
        error_msg = f"Sorry, the website {error} does not exist please enter the correct name of the website"
        messagebox.showerror(title="Invalid Website", message=error_msg)
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        is_update = messagebox.askyesno(title= f"Update {website_to_update}", message= question)
        if is_update:
            add_password_button.config(text="replace")
            email_entry.delete(0, tk.END)
            email_entry.insert(0, email)
            password_entry.delete(0, tk.END)
            password_entry.insert(0, password)
            new_email = email_entry.get()
            new_password = password_entry.get()
            data[website_to_update]["email"] = new_email
            data[website_to_update]["password"] = new_password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """saves the passwords and other details s into a json file as soon as add button is clicked"""
    website_name = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    message = f"These are the details you entered\nEmail: {email}\nPassword: {password}\nare these okay to save?"
    new_data = {
        website_name :
            {
                "email" : email,
                "password" : password
            }
    }
    if website_name and password :
        is_okay = messagebox.askokcancel(title=website_name, message=message)
        if is_okay:
            try:
                with open(file_name) as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = {}

            data.update(new_data)
            with open(file_name, "w") as file:
                json.dump(data, file, indent= 4) # json.dump(data, file) is used to write data to a json file
                website_entry.delete(0, tk.END) # clearing the entire fields
                password_entry.delete(0, tk.END)
                messagebox.showinfo(title= "Successful", message= "Details added successfully✔️")
    else:
        messagebox.showerror(title= "oops", message= "Do not leave any field empty!")
        password_entry.delete(0, tk.END)
        website_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #
# creating the window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)


# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries - using fixed widths
email_width = 40 # Width for email entry
entry_width = 25 # Width for website and password entries

website_entry = tk.Entry(width=entry_width)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="w", padx=5, pady=5)

email_entry = tk.Entry(width=email_width)
email_entry.insert(0, "olanisebemichael633@gmail.com") # to insert dummy texts into the field
email_entry.grid(row=2, column=1, columnspan=2, sticky="w", padx=5, pady=5)

password_entry = tk.Entry(width=entry_width)
password_entry.grid(row=3, column=1, sticky="w", padx=5, pady=5)

# Buttons
search_button = tk.Button(text= "Search", width= 15, command= search)
search_button.grid(row= 1, column= 2, sticky= "w", padx= 5, pady= 5)

gen_password_button = tk.Button(text="Generate", command= generate_password, width=15)
gen_password_button.grid(row=3, column=2, sticky="w", padx=5, pady=5)

add_password_button = tk.Button(text="Add", width=48, command= save)  # entry_width + 13 (button width + padding)
add_password_button.grid(row=4, column=0, columnspan=3, pady=10)

update_button = tk.Button(text= "Update", width= 24, command= update)
update_button.grid(row= 5, column= 0)

delete_button = tk.Button(text= "Delete", width= 24, command= delete)
delete_button.grid(row= 5, column= 2)

window.mainloop()