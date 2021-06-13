from os import PRIO_PGRP
from typing import Text
import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size=(500,700)

Builder.load_file("calc.kv")

class MyLayout(Widget):
    def clear_last(self):
        text = self.ids.calc_input.text
        text = text[:-1]
        self.ids.calc_input.text = text
        

    def clear(self):
        self.ids.calc_input.text = ""


    def add_number(self, i):
        if self.ids.calc_input.text == "0":
            self.clear()
        self.ids.calc_input.text = self.ids.calc_input.text+str(i)

    def negative_positive(self):
        if "-" in self.ids.calc_input.text:
            remove_sign = self.ids.calc_input.text
            remove_sign = remove_sign[1:]
            self.ids.calc_input.text = remove_sign
        else:
            self.ids.calc_input.text = str("-")+ self.ids.calc_input.text

    def dot(self):
        text = self.ids.calc_input.text
        if "." in text:
            pass
        else:
            self.ids.calc_input.text = self.ids.calc_input.text + "."
    def equal(self):
        num = self.ids.calc_input.text
         
        if "+" in num:
            num_list = num.split("+")
            j = 0
            for i in num_list:
                j = j + int(i)

            self.ids.calc_input.text = str(j)

        if "-" in num:
            num_list = num.split("-")
            j = 0
            for i in num_list:
                if j == 0:
                    j = float(i)
                else:
                    j = j - float(i)
            self.ids.calc_input.text = str(j)

        if "x" in num:
            num_list = num.split("x")
            j = 0
            for i in num_list:
                for i in num_list:
                    if j == 0:
                        j = float(i)
                    else:
                        j = j*float(i)
            self.ids.calc_input.text = str(j)

    #     if "/" in num:
    #         num_list = num.split("+")
    #         j = 0
    #         for i in num_list:
    #             j = j / float(i)

    #         self.ids.calc_input.text = str(j)

    

class CalculatorApp(App):
    def build(self):
        
        return MyLayout()


if __name__ == "__main__":
    CalculatorApp().run()