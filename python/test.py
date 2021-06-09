from tkinter import Label
from typing import Text
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class Music_Player(App):
    def build(self):
        
        return Label(text="Hello World")


if __name__ == "__main__":
    Music_Player().run()