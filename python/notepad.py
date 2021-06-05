import tkinter 
import os 
from tkinter import *
  
from tkinter.messagebox import *

from tkinter.filedialog import *

root = bg =  font = 0

def open():
    pass 

def create_new():
    pass

def close():
    exit(0)

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

    root = Tk()
    root.title("Notepad")
    
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New")
    filemenu.add_command(label="Open")
    filemenu.add_command(label="Save")
    filemenu.add_command(label="Save as...")

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=exit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo")

    editmenu.add_separator()

    editmenu.add_command(label="Cut")
    editmenu.add_command(label="Copy")
    editmenu.add_command(label="Paste")
    editmenu.add_command(label="Delete")
    editmenu.add_command(label="Select All")

    menubar.add_cascade(label="Edit", menu=editmenu)
    
    
    root.config(menu=menubar)
    root.geometry("950x750")
    root.mainloop()
