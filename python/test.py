from os import terminal_size
from tkinter import *

root = Tk()
root.title("Transparent BG!")
root.geometry("1270x720")

root.attributes("-alpha", 0)

Label(root, text="hello").pack()

root.mainloop()