from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder



Builder.load_file("practice.kv")

class MyGridLayout(Widget):

    Name = ObjectProperty("")
    Num = ObjectProperty("")
    Age = ObjectProperty("")
    
    def press(self):
            name = self.Name
            num = self.Num
            age = self.Age

            print(f"You are {name}\ncode no. {num}\nAge is {age}")
            
            self.Name = ""
            self.Num = ""
            self.Age = ""


class PracticeApp(App):
    def build(self):
        
        return MyGridLayout()


if __name__ == "__main__":
    PracticeApp().run()