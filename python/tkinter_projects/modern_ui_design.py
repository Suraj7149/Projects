from tkinter import *
#from ctypes import windll



root = Tk()
root.geometry("800x600+75+75")
root.overrideredirect(True)

LGRAY = '#3e4042' # button color effects in the title bar (Hex color)
DGRAY = '#25292e' # window background color               (Hex color)
RGRAY = '#10121f' # title bar color                       (Hex color)


title_bar = Frame(root, bg=RGRAY, relief="raised", bd=0,highlightthickness=0)
title_bar.pack(fill=X)

maximized = False
root.config(bg=DGRAY)

def maximize(e):
    global maximized
    if maximized == False:
        #root.state('zoomed')
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        expand.config(text=" 🗗 ")
        maximized = True
    elif maximized == True:
        root.geometry("800x600+75+75")
        expand.config(text=' 🗖 ')
        maximized = False
        
def minimize():
    global maximized
    if maximized == True:
        root.geometry("800x600+75+75")
        expand.config(text=' 🗖 ')
        maximized = False
    elif maximized == False:        
        root.geometry(f"-{2000}-{0}")


def move_app(e):
    x = int(e.x_root) - 400
    y = int(e.y_root) - 15
    root.geometry(f"+{x}+{y}")


def close_fun(e):
    quit()


Label(title_bar, text ="Hello UI", bg=RGRAY, fg = "White",font=("calibri", 12)).pack(side=LEFT)
close = Button(title_bar, text='  x  ', command=lambda: close_fun(1),bg=RGRAY,padx=6,pady=0,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
close.pack(side=RIGHT, padx=2, pady= 2)
expand = Button(title_bar, text=' 🗖 ',command=lambda: maximize(1),bg=RGRAY,padx=5,pady=0,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
expand.pack(side=RIGHT, padx=2, pady= 2)
mini = Button(title_bar, text=' - ',command=minimize,bg=RGRAY,padx=7,pady=0,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
mini.pack(side=RIGHT, padx=2, pady= 2)


root.bind("<F11>",maximize)
root.bind("<Escape>",close_fun)

title_bar.bind("<B1-Motion>", move_app)

root.mainloop()