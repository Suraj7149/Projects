import tkinter 
import os 
from tkinter import *
  
from tkinter.messagebox import *

from tkinter.filedialog import *

root = bg =  font = 0

def run():
    global root
    root = Tk()
    root.title("Notepad")
    root.geometry("950x750")
    root.mainloop()

def open():
    pass 

def create_new():
    pass

def close():
    pass

def new_window():
    pass 

def save():
    pass 

def change_bg():
    global bg
    bg = 1
    pass

def change_font():
    global font
    font = 1
    pass

def word_warp():
    pass

if "__main__" == __name__:
    run()
