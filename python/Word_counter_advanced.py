# importing gui libs
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog


# function to open file and calculate the total number
# of words and return it.
def count(text_file, display):

    ''' opens file, count words and returns it.'''

    # opening
    selected_file = open(text_file, "r")
    total_words = 0

    # counting
    for i in selected_file.read().split():
        total_words = total_words + 1
    
    # return
    Label(display, text="Total Words are : " + str(total_words)).pack()


# fuction for displaying gui and calcuting the number for words    
def selection_window():

    # initializing the display as root class
    root = Tk()
    # assigining title
    root.title("Word Counter")
    Button(root, text="close", command=root.destroy).pack(side="bottom")
    # opening dialogue box to select file from anywhere from the computer.
    # by using the filename variable under the root class
    root.filename = filedialog.askopenfilename(initialdir="/", title="select a file",
                    filetypes=(("text files", "*.txt"),("all files","*.")))
    #displaying the outputs
    Label(root, text="Selected file is :- "+root.filename).pack()
    Label(root, text=count(root.filename, root)).pack()
    root.geometry("300x100")
    root.mainloop()

# main program
loop = True
while loop:
    
    choice = input(">>>")
    if choice.lower() == "word_count":
        selection_window()
    elif choice.lower() == "exit":
        break
    elif choice.lower() == "help":
        print("'word_count' to run word counter \n'help' to see commands \n'close' to exit program.")
    else:
        continue
