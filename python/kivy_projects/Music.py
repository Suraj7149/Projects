from kivy.animation import Animation
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
if os.path.exists("C://Music Player"):
        pass
else:
        os.mkdir("C://Music Player")
Window.size = (320, 600)


Builder.load_file("music.kv")

def startup():
        global file_path
        global files
        
        try:
                files = os.listdir("C://Music Player")
                print(files[1])
        except:
                root = Tk()
                file_path = filedialog.askopenfilename(title="Select Music Files to Play")
                root.destroy()
                list1 = file_path.split("/")
                list1.pop()
                file_path = ""
                for i in list1:
                        file_path = file_path + i + "\\"

                for i in os.listdir(file_path):
                        if (".mp3") in i:
                                files.append(i)

                for songs in files:
                        shutil.copy(file_path+"/"+songs, "C://Music Player")
        

        

class MusicScreen(Screen):
        def ask(self):
                startup()

        def minimize(self):
                pass
                #Window.size = (320, 600)

        def maximize(self):
                pass
                #Config.set('graphics', 'fullscreen', "True")

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