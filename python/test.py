from tkinter import * 
from tkinter import filedialog
from tkinter import font
from tkinter.font import Font

w = 800
h = 600
root = Tk()
root.geometry(f"{w}x{h}")
root.title("Notepad")


text_font = Font(family="Times New Roman", size=14, slant="italic")
Button_font = Font(family="Ubuntu", size=12, weight="bold")


menubar = Menu(root, fg ="white", bg="black", font=Button_font)
file = Menu(menubar, tearoff=0, fg ="white", bg="black", font=Button_font)
file.add_command(label="Save")   
file.add_command(label="Save as..")
file.add_command(label="Open")
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
root.resizable(0,0)
root.mainloop()