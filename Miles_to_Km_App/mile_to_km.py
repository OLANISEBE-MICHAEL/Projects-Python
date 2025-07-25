import tkinter as tk
CONVERT = 1.609

def convert_to_km():
    result = round(float(input.get()) * CONVERT, 2)
    label_3.config(text= f"{result}")

# creating the window
window = tk.Tk()
window.minsize(width= 300, height= 150)
window.config(padx= 80, pady= 60)
window.title("Miles to Kilometer")


# creating text entry
input = tk.Entry(width= 3)
input.focus()
input.grid(row= 0, column= 1)

# creating label
label_1 = tk.Label(text= "is equal to", font= ("Times New Roman", 12))
label_2 = tk.Label(text= "miles", font= ("Times New Roman", 12))
label_3 = tk.Label(text= "0", font= ("Times New Roman", 12))
label_4 = tk.Label(text= "km", font= ("Times New Roman", 12))

label_1.grid(row= 1, column= 0)
label_2.grid(row= 0, column= 2)
label_3.grid(row= 1, column= 1)
label_4.grid(row= 1, column= 2)

label_1.config(padx= 10)
label_3.config(padx= 30)

# creating the button
button = tk.Button(text= "Calculate", command= convert_to_km)
button.grid(row= 2, column= 1)

window.mainloop()
