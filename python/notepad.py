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
    root.title("Untitled")
    
    menubar = Menu(root)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", background="white")
    filemenu.add_command(label="Open", background="white")
    filemenu.add_command(label="New Window", background="white")
    filemenu.add_command(label="Save", background="white")
    filemenu.add_separator(background="white")
    filemenu.add_command(label="Exit", command=exit, background="white") 
    menubar.add_cascade(label="File", menu=filemenu, background="light blue")
    

    editmenu = Menu(menubar, tearoff=2)
    editmenu.add_command(label="Word wrap", background="white")
    editmenu.add_command(label="Clear all", background="white")
    editmenu.add_command(label="Select All", background="white")
    editmenu.add_command(label="Help", background="white")
    menubar.add_cascade(label="Edit", menu=editmenu, background="light blue")


    viewmenu = Menu(menubar, tearoff=1)
    viewmenu.add_command(label="Fullscreen", background="white")
    viewmenu.add_command(label="Change Background", background="white")
    viewmenu.add_command(label="Change Font", background="white")
    menubar.add_cascade(label="View", menu=viewmenu, background="light blue")
    
    scrollbar = Scrollbar(root, bg="black", bd=4, width=16)
    scrollbar.pack(side=RIGHT, fill=Y)

    mylist = Listbox(root, yscrollcommand = scrollbar.set )
    for     line in range(100):
        mylist.insert(END, "This is line number " + str(line))

    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )

    root.config(menu=menubar, background="white")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()
