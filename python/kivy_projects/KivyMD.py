from kivy import app
# MD stands for Material Design create and 
# stated by google as how a good add should look like. 

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("kivymd.kv")

class MyLayout(Widget):
    pass

class KivyMdApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    KivyMdApp().run()