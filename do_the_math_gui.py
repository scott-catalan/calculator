'''
# Project Creation Date: 8:04:37 PM, 2/14/2026
'''

import do_the_math_logic as l
import customtkinter as ctk
import tkinter as tk
import string as s

#----------------------|Themes|----------------------#
# Note - include a button that swaps between light mode and dark mode
# Note - include a dropdown menu somewhere where the user can pick between any theme in /themes

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("C:/Scott/Code/calculator/themes/forest.json")

#----------------------|App|----------------------#

app = ctk.CTk()
app.title("DoTheMath")
app.geometry("600x450")
app.resizable(False, False)

container = ctk.CTkFrame(app)
container.pack(fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

screens = {}

def add_screen(name):
    frame = ctk.CTkFrame(container)
    frame.grid(row=0, column=0, sticky="nsew")
    screens[name] = frame
    return frame
def show_screen(name):
    screens[name].tkraise()

#----------------------|Calculator Screen|----------------------#

calculator = add_screen("calculator")

button_val = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9",
    "=", ".", "0",
    "(", "×", "-",
    ")", "÷", "+",
    "^", "π", "log"
]

def append_calc(input):
    current = calc_entry.get()
    calc_entry.delete(0, tk.END)
    calc_entry.insert(0, current + input)

def validate(input):
    pass

def blocker(event):
    text = calc_entry.get()
    char = event.char.lower()
    
    blocked = s.ascii_letters
    if event.char == "l":

    if event.char in blocked:
        return "break"

calc_entry = ctk.CTkEntry(calculator, placeholder_text="0", width=578, height=100)
calc_entry.place(relx=0.5, rely=0.25, anchor="center")
calc_entry.bind("<Key>", blocker)

for i in range(len(button_val)):
    btn = ctk.CTkButton(calculator, text=f"{button_val[i]}", width=75, height=75, command=lambda val=button_val[i]: append_calc(val))
    btn.place(relx=(int(i/3)*0.14)+0.08, rely=(i%3*0.19)+0.51, anchor="center")

tabs = ctk.CTkSegmentedButton(calculator, values=["Calculator", "Conversions"])
tabs.place(relx=0.5, rely=0.075, anchor="center", relwidth=0.96333, relheight=0.1)

app.mainloop()