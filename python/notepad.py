# importing gui and time library for use
from tkinter import *
import datetime
import os


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
    root.geometry("900x550")

    # displaying year-month-date
    Label(root, text="Today is:- " + str(datetime.date.today())).pack()

    # generating text box
    my_text = Text(root, width=80, height=20, font=("Ubuntu", 14))
    my_text.pack(pady=10, padx=15)

    # frame for button as pack() and grid function don't work in one window
    button_frame = Frame(root)
    button_frame.pack()

    # clear text button
    clear_button = Button(button_frame, text="Clear All", command=clear)
    # arranging
    clear_button.grid(column=0)

    # Save button
    get_text_button = Button(button_frame, text="Save", command=save_file)
    get_text_button.grid(column=1, padx=10)

    # quit button
    quit_button = Button(button_frame, text="Quit", command=root.destroy)
    quit_button.grid(column=2, padx=10)

    root.resizable(0, 0)
    # looping to display the window
    root.mainloop()


if __name__ == "__main__":
    run()
