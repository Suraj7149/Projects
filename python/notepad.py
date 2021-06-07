from notepad import open_file
from tkinter import * 
from tkinter import filedialog
from tkinter import font
from tkinter.font import Font

w = 800
h = 600
root = Tk()
root.geometry(f"{w}x{h}")
root.title("Notepad")

def new_file():
    my_text.delete("1.0", END)
    root.title("New File - Notepad!")
    status_bar.config(text="New File - Unsaved     ")

def open_file():
    my_text.delete("1.0", END)
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*'),
        
    )
    # show the open file dialog
    f = filedialog.askopenfile(initialdir="/home/suraj/Desktop", title="Open files", filetypes=filetypes)
    # read the text file and show its content on the Text
    name = f
    status_bar.config(text=name)
    my_text.insert('1.0', f.readlines())

text_font = Font(family="Times New Roman", size=14, slant="italic")
Button_font = Font(family="Ubuntu", size=12, weight="bold")

status_bar = Label(root, text="Ready    ", font=Button_font, anchor=E)
status_bar.pack(fill=X,side=BOTTOM,)


menubar = Menu(root, fg ="white", bg="black", font=Button_font)
file = Menu(menubar, tearoff=0, fg ="white", bg="black", font=Button_font)
file.add_command(label="New", command=new_file)  
file.add_command(label="Save")   
file.add_command(label="Save as..")
file.add_command(label="Open", command=open_file)
file.add_command(label="Recent..")
file.add_command(label="Close", command=root.destroy)
file.add_separator()
file.add_command(label="Exit", command=root.destroy)
edit = Menu(menubar, tearoff=0, fg ="white", bg="black", font=Button_font)
edit.add_command(label="change Font")
edit.add_command(label="Change Background")
edit.add_command(label="Fullscreen")
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