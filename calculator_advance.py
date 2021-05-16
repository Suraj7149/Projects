from tkinter import *


def add():
    e.insert(END, "+")


def dot():
    e.insert(END, ".")


def sub():
    e.insert(END, "-")


def multi():
    e.insert(END, "*")


def divide():
    e.insert(END, "/")


def clear():
    e.delete(0, END)


def click(number):
    e.insert(END, number)


def equal():
    result = eval(e.get())
    e.delete(0, END)
    e.insert(0, result)


root = Tk()
root.title("Calculator")
root.geometry("358x340")

e = Entry(root, width=57, borderwidth=3)
e.grid(columnspan=4, row=0, column=0, pady=5, padx=5)

Button(root, text="clear", font=("Ubuntu", 15), height=2, width=23, command=lambda: clear()).grid(row=1, column=0,
                                                                                                  columnspan=3)
Button(root, text="/", font=("Ubuntu", 14), height=2, width=7, command=lambda: divide()).grid(row=1, column=3)

Button(root, text="=", font=("Ubuntu", 14), height=2, width=15, command=lambda: equal()).grid(row=5, column=2,
                                                                                                    columnspan=2)
Button(root, text=".", font=("Ubuntu", 14), height=2, width=7, command=lambda: dot()).grid(row=5, column=0)
Button(root, text="0", font=("Ubuntu", 14), height=2, width=7, command=lambda: click(0)).grid(row=5, column=1)
Button(root, text="1", font=("Ubuntu", 14), height=2, width=7, command=lambda: click(1)).grid(row=4, column=2)
Button(root, text="x", font=("Ubuntu", 14), height=2, width=7, command=lambda: multi()).grid(row=4, column=3)

Button(root, text="2", font=("Ubuntu", 14), height=2, width=7, command=lambda: click(2)).grid(row=4, column=1)
Button(root, text="3", font=("Ubuntu", 14), height=2, width=7, command=lambda: click(3)).grid(row=4, column=0)
Button(root, text="4", font=("Ubuntu", 14), height=2, width=7, command=lambda: click(4)).grid(row=3, column=2)
Button(root, text="+", font=("Ubuntu", 14), height=2, width=7, command=lambda: add()).grid(row=3, column=3)

Button(root, text="5", font=("Ubuntu", 14), height=2, width=7, command=lambda: click(5)).grid(row=3, column=1)
Button(root, text="6", font=("Ubuntu", 14), height=2, width=7, command=lambda: click(6)).grid(row=3, column=0)
Button(root, text="7", font=("Ubuntu", 14), height=2, width=7, command=lambda: click(7)).grid(row=2, column=2)
Button(root, text="-", font=("Ubuntu", 14), height=2, width=7, command=lambda: sub()).grid(row=2, column=3)

Button(root, text="8", font=("Ubuntu", 14), height=2, width=7, command=lambda: click(8)).grid(row=2, column=1)
Button(root, text="9", font=("Ubuntu", 14), height=2, width=7, command=lambda: click(9)).grid(row=2, column=0)

root.mainloop()
