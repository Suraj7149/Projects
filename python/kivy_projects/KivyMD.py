from kivy import app
# MD stands for Material Design create and 
# stated by google as how a good add should look like. 

from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file("kivymd.kv")

MainApp().run()
