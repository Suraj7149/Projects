from re import A
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file("switch.kv")

class MyLayout(Widget):
    def switch_click(self, switchObject, switchVlaue):
        if switchVlaue:
            self.ids.text1.text = "Switch is On"
        else: 
            self.ids.text1.text = "Switch is Off"

class SwitchApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    SwitchApp().run()