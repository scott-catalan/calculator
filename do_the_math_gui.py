'''
# Project Creation Date: 8:04:37 PM, 2/14/2026
'''

import do_the_math_logic as l
import customtkinter as ctk
import tkinter as tk
import os as o
from tkinter import font

#----------------------|Visuals|----------------------#

ctk.set_appearance_mode("dark")

themes_folder = o.path.join(o.path.dirname(__file__), "themes")
if o.path.exists(themes_folder):
    theme_files = [f.replace(".json", "").capitalize() for f in o.listdir(themes_folder) if f.endswith(".json")]
else:
    theme_files = []

current_theme = theme_files[0]
try:
    ctk.set_default_color_theme(f"{themes_folder}/{current_theme}.json")
except:
    ctk.set_default_color_theme("blue")
#----------------------|App|----------------------#

app = ctk.CTk()
app.title("DoTheMath")
app.geometry("600x450")
app.resizable(False, False)

screens = {}

title_font = ctk.CTkFont(family="Cynosure Straight", size=40, weight="bold")
button_font = ctk.CTkFont(family="HPSIMPLIFIED", size=20, weight="bold")
entry_font = ctk.CTkFont(family="HPSIMPLIFIED", size=30, weight="bold")
dropdown_font = ctk.CTkFont(family="HPSIMPLIFIED", size=15, weight="bold")

#----------------------|Build UI|----------------------#

def build_ui(active_theme=None):
    global container, calculator, calc_entry, themes, current_theme

    if active_theme:
        current_theme = active_theme
    for widget in app.winfo_children():
        widget.destroy()

    screens.clear()
    container = ctk.CTkFrame(app)
    container.pack(fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    def add_screen(name):
        frame = ctk.CTkFrame(container)
        frame.grid(row=0, column=0, sticky="nsew")
        screens[name] = frame
        return frame
    def show_screen(name):
        screens[name].tkraise()

    #----------------------|Calculator Screen|----------------------#

    calculator = add_screen("Calculator")

    button_val = [
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9",
        "=", ".", "0",
        "(", "×", "-",
        ")", "÷", "+",
        "^", "π", "log("
    ]

    def append_calc(user_input):
        text = calc_entry.get()
        if l.live_validate(text, user_input):
                calc_entry.insert(tk.END, user_input)
    def backspace(event):
        text = calc_entry.get()
        calc_entry.delete(0, tk.END)
        calc_entry.insert(0, text[:-1])
        return "break"
    def flash_error():
        original_color = calc_entry.cget("border_color")
        calc_entry.configure(border_color="red")
        app.after(200, lambda: calc_entry.configure(border_color=original_color))
    def trigger_calculate(event=None):
        text = calc_entry.get()
        
        if l.validate(text):
            result = l.calculate(text)
            if result is not False:
                calc_entry.delete(0, tk.END)
                calc_entry.insert(0, "{:g}".format(float(result)))
            else:
                flash_error()
        else:
            flash_error()
        return "break"
    def processor(event):
        user_input = calc_entry.get()
        allowed = "1234567890.^/*()-+lpx"
        abbv = {"l": "log(", "/": "÷", "x": "×", "*": "×", "p": "π"}

        if not event.char or event.char not in allowed:
            return "break"
        
        mapped_char = abbv.get(event.char, event.char)
        
        if not l.live_validate(user_input, mapped_char):
            return "break"

        if event.char in abbv:
            calc_entry.insert(tk.END, abbv[event.char])
            return "break"

    calc_entry = ctk.CTkEntry(calculator, placeholder_text="0", font=entry_font, width=578, height=100)
    calc_entry.place(relx=0.5, rely=0.26, anchor="center")
    calc_entry.bind("<Key>", processor)
    calc_entry.bind("<Return>", trigger_calculate)
    calc_entry.bind("<BackSpace>", backspace)

    for i in range(len(button_val)):
        val = button_val[i]
        if val == "=":
            cmd = lambda: trigger_calculate()
        else:
            cmd = lambda v=val: append_calc(v)

        btn = ctk.CTkButton(calculator, text=f"{button_val[i]}", font=button_font, width=75, height=75, command=cmd)
        btn.place(relx=(int(i/3)*0.14)+0.08, rely=(i%3*0.19)+0.51, anchor="center")

    themes = ctk.CTkOptionMenu(calculator, width=130, height=42, values=theme_files, font=dropdown_font, command=change_theme)
    themes.set(current_theme)
    themes.place(relx=0.79, rely=0.075, anchor="e")

    mode = ctk.CTkOptionMenu(
        calculator, 
        width=100, 
        height=42, 
        values=["Dark", "Light"], 
        font=dropdown_font,
        command=change_mode)
    mode.set(ctk.get_appearance_mode())
    mode.place(relx=0.98, rely=0.075, anchor="e")

    title = ctk.CTkLabel(calculator, text="DoTheMath", font=title_font)
    title.place(relx=0.02, rely=0.075, anchor="w")

    show_screen("Calculator")

#----------------------|Theme Change|----------------------#

def change_theme(choice):
    ctk.set_default_color_theme(f"{themes_folder}/{choice}.json")
    build_ui(active_theme=choice)

def change_mode(choice):
    ctk.set_appearance_mode(choice)

#----------------------|Start App|----------------------#

build_ui()
app.mainloop()