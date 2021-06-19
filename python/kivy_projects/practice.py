from os import WIFSIGNALED
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.size = (800,600)
Builder.load_file("slider.kv")

class MyLayout(Widget):
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
            #print(filename[0])
        except:
            pass

    def slide_it(self, *args):
        self.slide_text.text = str(int(args[1]))
        self.slide_text.font_size = str(int(args[1]) * 5)

class PracticeApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    PracticeApp().run()