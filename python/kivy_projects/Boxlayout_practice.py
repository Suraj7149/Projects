import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window

Builder.load_file("Float_Layout.kv")

class MyLayout(Widget):
    
    Window.size = (800,600)
    pass


class Float_LayoutApp(App):
    def build(self):
        
        return MyLayout()


if __name__ == "__main__":
    Float_LayoutApp().run()