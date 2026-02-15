'''
# Project Creation Date: 8:04:37 PM, 2/14/2026
'''

import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("C:/Scott/Code/calculator/themes/matrix.json")

app = ctk.CTk()
app.title("CalcULater")
app.geometry("400x500")
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

app.mainloop()