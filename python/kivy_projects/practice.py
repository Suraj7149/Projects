from os import WIFSIGNALED
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.size = (800,600)
Builder.load_file("image.kv")

class MyLayout(Widget):
    pass


class PracticeApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    PracticeApp().run()