#! /usr/bin/env python3
from tkinter import * 
from tkinter import filedialog
from tkinter import font
from tkinter.font import BOLD, Font
import easygui
from tkinter import colorchooser
from datetime import date
from tkinter import ttk



w = 800
h = 600
filetype = (
    ("Text Files", "*.txt"),
    ("All Files", "*.*")
)

LGRAY = '#3e4042' # button color effects in the title bar (Hex color)
DGRAY = '#25292e' # window background color               (Hex color)
RGRAY = '#10121f' # title bar color                       (Hex color)


day = "Today's Date:- "+str(date.today())
global file_path
file_path = None
global selected
selected = None
root = Tk()
root.geometry(f"{w}x{h}")
root.title("Notepad")
transparency_value = 0.7
root.attributes("-alpha", transparency_value)




def get_name(name):
    string1 = ''
    for i in range(1, len(name)):
        if name[-i] == "/":
            break
        else:
            string1 = string1+(name[-i])
            continue
    
    return string1[::-1]


def  save_file(input):
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="home/suraj/Desktop/Projects/", filetypes=filetype)
    if text_file:
        file_path = text_file
        name = text_file
        name = get_name(text_file)
        # status_bar.config(text=f'Saved: {text_file}\t\t'+str(day))
        root.title(f'{name}')

        text_file = open(text_file, "w")
        text_file.write(my_text.get(1.0, END))
        text_file.close()


def save(input):
    global file_path
    if file_path:
        text_file = open(file_path, "w")
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        root.title(get_name(file_path))
        # status_bar.config(text=f'Saved: {file_path}'+str(day))
    else:
        save_file(1)


def full(e):
    root.attributes("-fullscreen", True)


def default_view(e):
    root.attributes("-fullscreen", False)
    w = 800
    h = 600
    root.geometry(f"{w}x{h}")


def new_file(input):
    global file_path
    my_text.delete("1.0", END)
    root.title("New File - Notepad!")
    # status_bar.config(text="New File - Unsaved     \t\t"+str(day))
    file_path = False


def open_file(input):
    global file_path

    my_text.delete("1.0", END)
    
    # show the open file dialog
    file_path = easygui.fileopenbox()

    # read the text file and show its content on the Text
    f = open(file_path, "r")
    # status_bar.config(text=file_path+'\t\t'+str(day))
    root.title(get_name(file_path)+"(Read-Only-Mode)")

    my_text.insert('1.0', f.read())
    f.close()


def cut_fun(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            selected = my_text.selection_get()
            my_text.delete("sel.first", "sel.last")
    

def bold_text(e):
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.config(weight="bold")

    my_text.tag_configure("bold", font=bold_font)

    current_tags = my_text.tag_names("sel.first")

    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")

    else:
        my_text.tag_add("bold", "sel.first", "sel.last")


def italic_text(e):
    italic_font = font.Font(my_text, my_text.cget("font"))
    italic_font.config(slant="italic")
    
    my_text.tag_configure("italic", font = italic_font)

    current_tags = my_text.tag_names("sel.first")

    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")

    else:
        my_text.tag_add("italic", "sel.first", "sel.last")


def bold_italic_text(e):
    bold_italic_font = font.Font(my_text, my_text.cget("font"))
    bold_italic_font.config(weight="bold", slant="italic")
    my_text.tag_configure("bold_italic", font=bold_italic_font)

    current_tags = my_text.tag_names("sel.first")

    if "bold_italic" in current_tags:
        my_text.tag_remove("bold_italic", "sel.first", "sel.last")

    else:
        if "bold" or "italic" in current_tags:
            my_text.tag_remove("bold", "sel.first", "sel.last")
            my_text.tag_remove("italic", "sel.first", "sel.last")
        my_text.tag_add("bold_italic", "sel.first", "sel.last")


def paste_fun(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)
            root.clipboard_clear()
            root.clipboard_append(selected)


def copy_fun(e):
    global selected
    if e:
        selected = root.clipboard_get()

    if my_text.selection_get():
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)


def clear():
    my_text.delete(1.0, END)


def select_all(e):
    my_text.tag_add("sel", 1.0, END)


def change_bg():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)
        # status_bar.config(bg=my_color)
    

def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color)
        # status_bar.config(fg=my_color)

    
def change_font():
    my_color = colorchooser.askcolor()[1]
    color_font = font.Font(my_text, my_text.cget("font"))
    if my_color:
        my_text.tag_configure("colored", font = color_font, foreground=my_color)
        current_tags = my_text.tag_names("sel.first")

        if "colored" in current_tags:
            my_text.tag_remove("colored", "sel.first", "sel.last")

        else:
            my_text.tag_add("colored", "sel.first", "sel.last")
    

text_font = Font(family="Times New Roman", size=17)
Button_font = Font(family="Ubuntu", size=12, weight="bold")

# status_bar = Label(root, text="Ready    "+'\t\t'+str(day), font=Button_font, anchor=E)
# status_bar.pack(fill=X,side=BOTTOM)

def scale(x):
    root.attributes("-alpha", my_scale.get())

my_scale = ttk.Scale(root, from_=0.4, to=1.0, value=0.7,orient=HORIZONTAL, command=scale)
my_scale.pack(side=BOTTOM)
my_frame = Frame(root)
my_frame.pack(side=LEFT, fill="both")


text_scroll = Scrollbar(my_frame, width=13, bg="White")
text_scroll.pack(side=RIGHT, fill=Y)

Hori_text_scroll = Scrollbar(my_frame, orient="horizontal")
Hori_text_scroll.pack(side=BOTTOM, fill=X)

my_text = Text(my_frame, width=w, height=h, font=text_font, fg="white", bg=DGRAY, 
            selectbackground="orange", undo=True, yscrollcommand=text_scroll.set,
            wrap="none", xscrollcommand=Hori_text_scroll.set)
my_text.pack(side=LEFT, fill="both")

menubar = Menu(root, fg ="white", bg="black", font=Button_font)
file = Menu(menubar, tearoff=0, fg ="white", bg="black", font=Button_font)
file.add_command(label="New", command=lambda: new_file(1), accelerator="Ctrl + n")  
file.add_command(label="Save", command=lambda: save(1), accelerator="Ctrl + s")   
file.add_command(label="Save as..", command=lambda: save_file(1), accelerator="Ctrl + Shift + s")
file.add_command(label="Open", command=lambda: open_file(1), accelerator="Ctrl + o")
file.add_command(label="Clear All", command=clear, accelerator="Ctrl + Shift + D")
file.add_separator()
file.add_command(label="Exit", command=root.destroy, accelerator="Alt + F4")
edit = Menu(menubar, tearoff=0, fg ="white", bg="black", font=Button_font)
edit.add_command(label="Cut", command=lambda: cut_fun(False), accelerator="Ctrl + x")
edit.add_command(label="Copy", command=lambda: copy_fun(False), accelerator="Ctrl + c")
edit.add_command(label="Paste", command=lambda: paste_fun(False), accelerator="Ctrl + v")
edit.add_separator()
edit.add_command(label="Undo", command=my_text.edit_undo, accelerator="Ctrl + z")
edit.add_command(label="Redo", command=my_text.edit_undo, accelerator="Ctrl + y")
view = Menu(menubar, tearoff=0, fg ="white", bg="black", font=Button_font)
view.add_command(label="Highlighter", command=change_font)
view.add_command(label="Change Font Color", command=all_text_color)
view.add_command(label="Change Background", command=change_bg)
view.add_command(label="Fullscreen", command=lambda: full(1), accelerator="F11")
view.add_command(label="Bold", command=lambda: bold_text(1), accelerator="Ctrl + b")
view.add_command(label="Italic", command=lambda: italic_text(1), accelerator="Ctrl + i")
view.add_command(label="Bold-Italic", command=lambda: bold_italic_text(1), accelerator="Ctrl + i + b")
view.add_separator()
view.add_command(label="Default", command=lambda: default_view(1), accelerator="Esc")


menubar.add_cascade(label="File", menu=file)
menubar.add_cascade(label="Edit", menu=edit)
menubar.add_cascade(label="View", menu=view)


root.bind("<Control-Key-x>", cut_fun)
root.bind("<Control-Key-c>", copy_fun)
root.bind("<Control-Key-y>", paste_fun)
root.bind("<Control-Key-o>", open_file)
root.bind("<Control-Key-n>", new_file)
root.bind("<Control-Key-s>", save)
root.bind("<Control-Key-S>", save_file)
root.bind("<F11>", full)
root.bind("<Escape>", default_view)
root.bind("<Control-Key-b>", bold_text)
root.bind("<Control-Key-i>", italic_text)
root.bind("<Control-Key-a>", select_all)

text_scroll.config(command=my_text.yview)
Hori_text_scroll.config(command=my_text.xview)
root.config(menu=menubar)
# root.resizable(0,0)
root.mainloop()
