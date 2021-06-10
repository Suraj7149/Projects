from ast import Num
from kivy.core import text
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGridLayout(Widget):

    Name = ObjectProperty(None)
    Num = ObjectProperty(None)
    Age = ObjectProperty(None)
    # def __init__(self, **kwargs):

    #     super(MyGridLayout, self).__init__(**kwargs)
    #     self.cols = 1
    #     self.row_force_default = True
    #     self.row_default_height=120
    #     self.col_force_default=True
    #     self.col_default_width=100
    
    #     self.top_grid = GridLayout(
    #         row_force_default = True,
    #         row_default_height=40,
    #         col_force_default=True,
    #         col_default_width=100
    #     )
    #     self.top_grid.cols = 2

    #     self.top_grid.add_widget(Label(text="Name: "))
    #     self.name = TextInput(multiline=False)
    #     self.top_grid.add_widget(self.name)

    #     self.top_grid.add_widget(Label(text="Number: "))
    #     self.number = TextInput(multiline=False)
    #     self.top_grid.add_widget(self.number)

    #     self.top_grid.add_widget(Label(text="Age: "))
    #     self.age = TextInput(multiline=False)
    #     self.top_grid.add_widget(self.age)

    #     self.add_widget(self.top_grid)

    #     self.submit = Button(text="Submit")
    #     self.submit.background_color = (0,2,2,.5)
    #     self.submit.bind(on_press=self.press)
    #     self.add_widget(self.submit)

    #     self.close = Button(text="Close Button")
    #     self.close.bind(on_press=exit)
    #     self.add_widget(self.close)

    def press(self):
            name = self.Name.text
            number = self.Num.text
            age = self.Age.text

            self.add_widget(Label(text=f"You are {name}\ncode no. {number}\nAge is {age}", font_size = 16))
            
            self.name.text = ""
            self.number.text = ""
            self.age.text = ""


class PracticeApp(App):
    def build(self):
        
        return MyGridLayout()


if __name__ == "__main__":
    PracticeApp().run()