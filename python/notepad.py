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

def run():
    global root
    global my_text
    

    # initializing window 
    root = Tk()
    root.title("Personal Diary")
    root.minsize(height=500, width=500)

    text_font = Font(family="Times New Roman", size=14, slant="italic")
    Button_font = Font(family="Ubuntu", size=10, slant="italic", weight="bold")

    # generating text box
    my_text = Text(root, width=80, height=20, font=text_font)
    my_text.pack(pady=10, padx=15)
    
    # displaying year-month-date
    Label(root, text="Today is:- " + str(datetime.date.today()), font=text_font).pack(padx=5, pady=5, side=RIGHT)

    clear_button = Button(root, text="Delete", font=Button_font, command=clear)
    open_button = Button(root, text="Open",font=Button_font,  command=open_file())
    get_text_button = Button(root, text="Save",font=Button_font,  command=save_file)
    change_bg_button = Button(root, text="Edit",font=Button_font,  command=change_bg())
    quit_button = Button(root, text="Quit",font=Button_font,  command=root.destroy)
    change_font_button = Button(root, text="Fullscreen",font=Button_font,  command=change_font())


    get_text_button.pack(padx=10, pady=3, side=LEFT, anchor=SE)
    open_button.pack(padx=10, pady=3, side=LEFT, anchor=SE)
    quit_button.pack(padx=10, pady=3, side=LEFT, anchor=SE)
    change_bg_button.pack(padx=10, pady=3, side=LEFT, anchor=SE)
    change_font_button.pack(padx=10, pady=3, side=LEFT, anchor=SE)
    clear_button.pack(padx=10, pady=3, side=LEFT, anchor=SE)

    root.resizable(0, 0)
    # looping to display the window
    root.mainloop()


if __name__ == "__main__":
    run()
