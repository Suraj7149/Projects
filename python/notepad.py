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
    
    file_menu_title = edit_menu_title = StringVar()
    file_menu_title.set("File")
    edit_menu_title.set("Edit")
    
    file_drop_menu = OptionMenu(root, file_menu_title, "Open", "New", "New window", "Save")
    file_drop_menu.grid(row=0, column=0)

    edit_drop_menu = OptionMenu(root, edit_menu_title, "Change font", "Change background", "Word Counter")
    edit_drop_menu.grid(row=0, column=1)

    Close = Button(root, text="Close", command=close())
    Close.grid(padx=5, pady=5, row=0, column=2)

    root.geometry("950x750")
    root.mainloop()

def open():
    pass 

def create_new():
    pass

def close(e):
    exit()

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
