# Import required libraries.
from tkinter import *
import customtkinter
import openai
import os
import pickle

# Create the main window of the app.
app = customtkinter.CTk()
app.title("PyChat")
app.geometry("800x600")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Create frame for the textbox
textbox_frame = customtkinter.CTkFrame(app)
textbox_frame.pack(pady=20)

# Create the textbox for the responses
textbox = Text(textbox_frame, bg="#343638", width=65, bd=1, fg="#d6d6d6", relief="flat", wrap=WORD,
               selectbackground="#1f538d")
textbox.grid(row=0, column=0)

# Add a scrollbar to the response widget
response_scrollbar = customtkinter.CTkScrollbar(textbox_frame, command=textbox.yview)
response_scrollbar.grid(row=0, column=1, sticky="ns")

# Add the scrollbar inside the response widget
textbox.configure(yscrollcommand=response_scrollbar.set)

# run the main app
app.mainloop()
