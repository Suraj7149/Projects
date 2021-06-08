from tkinter import * 
from tkinter import filedialog
from tkinter import font
from tkinter.font import Font
import easygui

w = 800
h = 600
filetype = (
    ("Text Files", "*.txt"),
    ("All Files", "*.*")
)
file_path = None
root = Tk()
root.geometry(f"{w}x{h}")
root.title("Notepad")

def get_name(name):
    string1 = ''
    for i in range(1, len(name)):
        if name[-i] == "/":
            break
        else:
            string1 = string1+(name[-i])
            continue
    
    return string1[::-1]

def  save_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="home/suraj/Desktop/Projects/", filetypes=filetype)
    if text_file:
        file_path = text_file
        name = text_file
        name = get_name(text_file)
        status_bar.config(text=f'Saved: {text_file}')
        root.title(f'{name}')

        text_file = open(text_file, "w")
        text_file.write(my_text.get(1.0, END))
        text_file.close()


def save():
    global file_path
    if file_path:
        text_file = open(file_path, "w")
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        root.title(get_name(file_path))
        status_bar.config(text=f'Saved: {file_path}')
    else:
        save_file()



def full():
    w = root.winfo_screenwidth
    h = root.winfo_screenheight

    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))


def new_file():
    my_text.delete("1.0", END)
    root.title("New File - Notepad!")
    status_bar.config(text="New File - Unsaved     ")
    file_path = False


def open_file():
    global file_path

    my_text.delete("1.0", END)
    
    # show the open file dialog
    file_path = easygui.fileopenbox()

    # read the text file and show its content on the Text
    f = open(file_path, "r")
    status_bar.config(text=file_path)
    root.title(get_name(file_path)+"(Read-Only-Mode)")

    my_text.insert('1.0', f.read())
    f.close()

text_font = Font(family="Times New Roman", size=14, slant="italic")
Button_font = Font(family="Ubuntu", size=12, weight="bold")

status_bar = Label(root, text="Ready    ", font=Button_font, anchor=E)
status_bar.pack(fill=X,side=BOTTOM,)


menubar = Menu(root, fg ="white", bg="black", font=Button_font)
file = Menu(menubar, tearoff=0, fg ="white", bg="black", font=Button_font)
file.add_command(label="New", command=new_file)  
file.add_command(label="Save", command=save)   
file.add_command(label="Save as..", command=save_file)
file.add_command(label="Open", command=open_file)
file.add_command(label="Recent..")
file.add_command(label="Close", command=root.destroy)
file.add_separator()
file.add_command(label="Exit", command=root.destroy)
edit = Menu(menubar, tearoff=0, fg ="white", bg="black", font=Button_font)
edit.add_command(label="change Font")
edit.add_command(label="Change Background")
edit.add_command(label="Fullscreen", command=full)
edit.add_command(label="Bold")
edit.add_command(label="Italic")
edit.add_separator()
edit.add_command(label="Reset")


menubar.add_cascade(label="File", menu=file)
menubar.add_cascade(label="Edit", menu=edit)


my_frame = Frame(root)
my_frame.pack(side=LEFT, fill="both")


text_scroll = Scrollbar(my_frame, width=13, bg="White")
text_scroll.pack(side=RIGHT, fill=Y)


my_text = Text(my_frame, width=w, height=h, font=text_font, fg="white", bg="black", selectbackground="orange", undo=True, yscrollcommand=text_scroll.set)
my_text.pack(side=LEFT, fill="both")


text_scroll.config(command=my_text.yview)
root.config(menu=menubar)
# root.resizable(0,0)
root.mainloop()