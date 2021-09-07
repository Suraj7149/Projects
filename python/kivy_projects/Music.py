from tkinter.font import BOLD
from kivy.animation import Animation
from kivy.core import window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.animation import Animation
from tkinter import * 
from tkinter import filedialog
import os
import shutil
from kivy.core.window import Window


file_path = None
files = []


if os.path.exists("C://Music Player//Songs") and os.path.exists("C://Music Player//Images"):
        pass
else:
        os.mkdir("C://Music Player//Songs")
        os.mkdir("C://Music Player//Images")


maximized = False
song_name = "Song Name"
Window.size = (320, 600)
Builder.load_file("music.kv")


def startup():
        global file_path
        global files
        global song_name
        root = Tk()
        file_path = filedialog.askopenfilename(title="Select Music Files to Play")
        root.destroy()
        list1 = file_path.split("/")
        song_name = list1.pop()
        file_path = ""
        for i in list1:
                file_path = file_path + i + "\\"

        for i in os.listdir(file_path):
                if (".mp3") in i:
                        files.append(i)

        for songs in files:
                shutil.copy(file_path+"/"+songs, "C://Music Player//Songs")
        

        

class MusicScreen(Screen):
        def ask(self):
                startup()
                print(len(song_name))
                if len(song_name) > 15:
                        self.ids.song_name.font_size = "14sp"
                elif len(song_name) > 20:
                        self.ids.song_name.font_size = 2
                self.ids.song_name.text = song_name.replace(".mp3", " ")

        def minimize(self):
                root = Tk()
                root.geometry("800x600+75+75")
                root.overrideredirect(True)
                root.config(bg="#25292e")

                LGRAY = '#3e4042' # button color effects in the title bar (Hex color)
                DGRAY = '#25292e' # window background color               (Hex color)
                RGRAY = '#10121f' # title bar color                       (Hex color)


                title_bar = Frame(root, bg=RGRAY, relief="raised", bd=0,highlightthickness=0)
                title_bar.pack(fill=X)

                

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
                        

                def move_app(e):
                        x = int(e.x_root) - 400
                        y = int(e.y_root) - 15
                        root.geometry(f"+{x}+{y}")


                def close_fun(e):
                        root.destroy()


                Label(title_bar, text ="Songs List", bg=RGRAY, fg = "White",font=("calibri", 12)).pack(side=LEFT)
                close = Button(title_bar, text='  x  ', command=lambda: close_fun(1),bg=RGRAY,padx=6,pady=0,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
                close.pack(side=RIGHT, padx=2, pady= 2)
                expand = Button(title_bar, text=' 🗖 ',command=lambda: maximize(1),bg=RGRAY,padx=5,pady=0,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
                expand.pack(side=RIGHT, padx=2, pady= 2)

                scrollbar = Scrollbar(root, width=15, bg="#25292e")
                scrollbar.pack(side=RIGHT, fill=Y)

                listbox = Listbox(root, bg="#25292e", fg="White", font=("calibri", 14), yscrollcommand= scrollbar.set)
                                
                for i in os.listdir("C://Music Player//Songs"):
                        listbox.insert(END, i)
                        #Button(root, text=str(i), bg="#25292e", fg = "White",font=("calibri", 12)).pack()

                listbox.pack(fill=BOTH, expand=1)
                scrollbar.config(command=listbox.yview)

                def delete():
                        for i in listbox.curselection():
                                os.remove("C://Music Player//Songs"+"//"+listbox.get(i))
                                listbox.delete(i)
                        


                delete_button = Button(root, width = 50, text="Delete Song", bg=LGRAY, fg = "White",font=("calibri", 12, BOLD), command=delete)
                delete_button.pack(side=LEFT, expand=0.5)

                play_button = Button(root, width = 50, text="Play Song", bg=LGRAY, fg = "White",font=("calibri", 12, BOLD))
                play_button.pack(side= RIGHT, expand=0.5)

                root.bind("<F11>",maximize)
                root.bind("<Escape>",close_fun)

                title_bar.bind("<B1-Motion>", move_app)

                root.mainloop()
                

        def maximize(self):
                root = Tk()
                file = filedialog.askopenfilename(title="Select Music Files to Play")
                root.destroy()
                # list1 = file.split("/")
                # list1.pop()
                # file = ""
                # for i in list1:
                #         file = file+ i + "\\"
                self.ids.bg_image.source = file
                self.ids.music.source = file
                

class SongCover(MDBoxLayout):
        
        angle = NumericProperty()
        anim = Animation(angle= - 360, d=3, t="linear")
        anim += Animation(angle=0, d=0, t="linear")
        anim.repeat = True
        
        progress = Animation(value = 100, d=100, t="linear")

        def rotate(self):

                if self.anim.have_properties_to_animate(self):
                        self.anim.stop(self)
                        self.progress.stop(self.widget)
                else:
                        self.anim.start(self)
                        self.progress.stop(self.widget)

        def play(self, widget):
                
                self.widget = widget
                self.progress.start(widget)
                self.rotate()


class MainApp(MDApp):
        def build(self):
                Window.borderless = True
                self.theme_cls.theme_style = "Dark"
                return MusicScreen()


#startup()
MainApp().run()