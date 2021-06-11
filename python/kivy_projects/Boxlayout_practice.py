import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window


Builder.load_file("box.kv")

class MyLayout(Widget):
    
    Window.size = (1280,720)
    def press(self):
        name = self.ids.name_input.text
        
        self.ids.name_label.text = "Your name:- "+name+"\nWelcome to the Family."

class BoxApp(App):
    def build(self):
        
        return MyLayout()


if __name__ == "__main__":
    BoxApp().run()