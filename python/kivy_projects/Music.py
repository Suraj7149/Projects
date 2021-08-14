from kivy.animation import Animation
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.animation import Animation
Window.size = (320, 600)


Builder.load_file("music.kv")

class MusicScreen(Screen):
        pass

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
                self.theme_cls.theme_style = "Dark"
                return MusicScreen()


MainApp().run()