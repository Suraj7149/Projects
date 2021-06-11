import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file("box1.kv")

class MyLayout(Widget):
    pass


class BoxApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    BoxApp().run()