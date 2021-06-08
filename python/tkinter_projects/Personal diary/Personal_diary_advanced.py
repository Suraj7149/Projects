# importing gui and time library for use
from tkinter import *
import datetime
import os

if os.path.exists("C:\\Personal_Diary"):
    pass
    print("directory already exists")
else:
    os.mkdir("C:\\Personal_Diary")
    print("directory created.")


# creating a function to clear
def clear():
    # this statement will delete from start till end.
    my_text.delete(1.0, END)


# func. to save the text before clearing or quitting
def get_text():
    file = open("C:\\Personal_Diary\\" + str(datetime.date.today()) + ".txt", "w")
    file.writelines(my_text.get(1.0, END))
    file.close()
    my_text.delete(1.0, END)


def run():
    global root
    global my_text
    # initializing window 
    root = Tk()
    root.title("Personal Diary")
    root.geometry("700x535")

    # displaying year-month-date
    Label(root, text="Today is:- " + str(datetime.date.today())).pack()

    # generating text box
    my_text = Text(root, width=60, height=20, font=("Ubuntu", 14))
    my_text.pack(pady=20)

    # frame for button as pack() and grid function don't work in one window
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


if __name__ == "__main__":
    loop = True
    while loop:

        choice = input(">>>")
        if choice.lower() == "run":
            run()
        elif choice.lower() == "exit":
            break

        elif choice.lower() == "show":
            for file in os.listdir("C:\\Personal_Diary"):
                if file.endswith(".txt"):
                    print("diary file :" + file)

        elif choice.lower() == "view":
            selection = input("enter the file name:- ")
            print("")
            with open("C:\\Personal_Diary\\"+selection+".txt", "r") as f:
                for i in f.readlines():
                    print(i)

        elif choice.lower() == "help":
            print('"run" to start the personal diary window.\n"exit" to exit dairy.\n"show" to see all files.\n"view" to see the content of selected file."')
        else:
            continue
