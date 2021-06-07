# importing gui and time library for use
from tkinter import *
import datetime
import os
from tkinter.font import Font


try:
    if os.path.exists("Notepad"):
        pass
    else:
        os.mkdir("Notepad")
except FileNotFoundError:
    if os.path.exists("C:/Notepad"):
        pass
    else:
        os.mkdir("C:/Notepad")

# creating a function to clear
def clear():
    # this statement will delete from start till end.
    my_text.delete(1.0, END)


# func. to save the text before clearing or quitting
def save_file():
    if os.path.exists("C:\\Notepad\\") or os.path.exists("Notepad"):
        file = open("Notepad/" + str(datetime.date.today())+ ".txt", "w")
        file.writelines(my_text.get(1.0, END))
        file.close()
        my_text.delete(1.0, END)
    else:

        try:
            if os.path.exists("Notepad"):
                pass
            else:
                os.mkdir("Notepad")
        except FileNotFoundError:
            if os.path.exists("C:/Notepad"):
                pass
            else:
                os.mkdir("C:/Notepad")


def open_file():
    pass


def change_bg():
    pass


def change_font():
    pass 

def bold():
    pass

def italic():
    pass

def fullscreen():
    
    print(root.winfo_screenwidth(), root.winfo_screenheight())


def run():
    global root
    global my_text
    

    # initializing window 
    root = Tk()
    root.title("Personal Diary")
    root.geometry("700x500")
    
    menubar = Menu(root)
    file = Menu(menubar, tearoff=0)
    file.add_command(label="Save", command=save_file)
    file.add_command(label="Save as..")
    file.add_command(label="Open")
    file.add_command(label="Recent..")
    file.add_command(label="Close", command=clear)
    file.add_separator()
    file.add_command(label="Exit", command=root.destroy)

    edit = Menu(menubar, tearoff=0)
    edit.add_command(label="change Font", command=change_font)
    edit.add_command(label="Change Background", command=change_bg)
    edit.add_command(label="Fullscreen", command=fullscreen)
    edit.add_command(label="Bold", command=bold)
    edit.add_command(label="Italic", command=italic)

    menubar.add_cascade(label="File", menu=file)
    menubar.add_cascade(label="Edit", menu=edit)
    
    text_font = Font(family="Times New Roman", size=14, slant="italic")
    Button_font = Font(family="Ubuntu", size=10, slant="italic", weight="bold")
    
    # Label(root, text="Today is:- " + str(datetime.date.today()), font=text_font).pack(padx=5, side=TOP)

    # generating text box
    my_text = Text(root, font=text_font)
    my_text.pack()
    
    root.config(menu=menubar)
    # root.resizable(0, 0)
    # looping to display the window
    root.mainloop()


if __name__ == "__main__":
    run()
