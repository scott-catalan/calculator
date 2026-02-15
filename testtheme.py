'''
# Project Creation Date: 9:46:23 PM, 2/14/2026
'''

import customtkinter as ctk
from tkinter import Tk

# Initialize app
ctk.set_appearance_mode("Light")  # Light/Dark/Custom
ctk.set_default_color_theme("C:/Scott/Code/calculator/themes/frost.json")  # Placeholder; your theme can be loaded here
app = ctk.CTk()
app.title("CTk Widget Playground")
app.geometry("900x700")

# ----- Frames -----
main_frame = ctk.CTkFrame(app, corner_radius=6)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# ----- Labels -----
label = ctk.CTkLabel(main_frame, text="CTk Label Example")
label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# ----- Entry -----
entry = ctk.CTkEntry(main_frame, placeholder_text="CTk Entry Example")
entry.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# ----- Button -----
button = ctk.CTkButton(main_frame, text="CTk Button")
button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# ----- CheckBox -----
checkbox = ctk.CTkCheckBox(main_frame, text="CTk CheckBox")
checkbox.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# ----- Switch -----
switch = ctk.CTkSwitch(main_frame, text="CTk Switch")
switch.grid(row=4, column=0, padx=10, pady=10, sticky="w")

# ----- RadioButton -----
radio_var = ctk.IntVar(value=1)
radiobutton1 = ctk.CTkRadioButton(main_frame, text="Option 1", variable=radio_var, value=1)
radiobutton2 = ctk.CTkRadioButton(main_frame, text="Option 2", variable=radio_var, value=2)
radiobutton1.grid(row=5, column=0, padx=10, pady=5, sticky="w")
radiobutton2.grid(row=6, column=0, padx=10, pady=5, sticky="w")

# ----- Slider -----
slider = ctk.CTkSlider(main_frame, from_=0, to=100)
slider.grid(row=7, column=0, padx=10, pady=10, sticky="we")

# ----- ProgressBar -----
progress = ctk.CTkProgressBar(main_frame)
progress.set(0.5)
progress.grid(row=8, column=0, padx=10, pady=10, sticky="we")

# ----- OptionMenu -----
optionmenu = ctk.CTkOptionMenu(main_frame, values=["Option A", "Option B", "Option C"])
optionmenu.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# ----- ComboBox -----
combobox = ctk.CTkComboBox(main_frame, values=["Choice 1", "Choice 2", "Choice 3"])
combobox.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# ----- SegmentedButton -----
seg_button = ctk.CTkSegmentedButton(main_frame, values=["Tab1", "Tab2", "Tab3"])
seg_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# ----- TextBox -----
textbox = ctk.CTkTextbox(main_frame, width=300, height=100)
textbox.insert("0.0", "CTk TextBox Example")
textbox.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# ----- ScrollableFrame -----
scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=300, height=150)
scrollable_frame.grid(row=4, column=1, rowspan=5, padx=10, pady=10, sticky="nsew")
for i in range(10):
    ctk.CTkLabel(scrollable_frame, text=f"Scrollable Item {i+1}").pack(padx=5, pady=5)

# Make columns stretch
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

app.mainloop()
