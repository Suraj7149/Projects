import os 
from tkinter import *
import datetime
import time

def greet():
    welcome_screen = Tk()
    welcome_screen.title("Greeting.")
    welcome_screen.geometry("230x60")
    Label(welcome_screen, text="Sir, Good Morning.", font=("Ubuntu", 16)).pack()
    Label(welcome_screen, text="Date", font=("Ubuntu", 13)).pack()
    welcome_screen.after(3000, welcome_screen.destroy)

    welcome_screen.mainloop()
if "__main__" == __name__:
    greet()
