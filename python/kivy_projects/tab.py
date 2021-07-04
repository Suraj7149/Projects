from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty

Builder.load_file("multitab.kv")

class MyLayout(TabbedPanel):
    pass

class TabbedApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    TabbedApp().run()