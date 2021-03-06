from kivy.config import Config
Config.set("graphics", "position", "custom")
Config.set('graphics', 'borderless', 'True')
#Config.set('graphics', 'fullscreen', 'auto')
Config.set("graphics", "left", 400)
Config.set("graphics", "top", 100)
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

class MainApp(MDApp):
    def build(self):
        Window.borderless = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("custombar.kv")


MainApp().run()