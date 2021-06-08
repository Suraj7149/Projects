# importing gui and time library for use
from tkinter import *
import datetime

# creating a function to clear
def clear():
    # this statement will delete from start till end.
    my_text.delete(1.0, END)

# func. to save the text before clearing or quitting
def get_text():
    file = open(str(datetime.date.today())+".txt", "a")
    file.writelines(my_text.get(1.0, END))
    file.close()
    my_text.delete(1.0, END)

# initializing window 
root = Tk()
root.title("Personal Diary")
root.geometry("700x535")

# displaying year-month-date
Label(root, text="Today is:- " + str(datetime.date.today())).pack()

# generating text box
my_text = Text(root, width=60, height=20, font=("Ubuntu", 14))
my_text.pack(pady=20)

# frame for button as pack() and grid funtion dosen't work in one window
button_frame = Frame(root)
button_frame.pack()

# clear text button
clear_button = Button(button_frame, text="Clear All", command=clear)
# arranging
clear_button.grid(row=0, column=0)

# Save button
get_text_button = Button(button_frame, text="Save", command=get_text)
get_text_button.grid(row=0, column=1, padx=10)

# quit button
quit_button = Button(button_frame, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=2, padx=10)

# looping to display the window
root.mainloop()
