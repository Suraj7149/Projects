from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("800x600")

root.attributes("-alpha", 0.5)

def scale(x):
    root.attributes("-alpha",my_slider.get())

my_slider = ttk.Scale(root,from_=0.1, to=1.0, value = 0.7, command=scale)
my_slider.pack()

root.mainloop()