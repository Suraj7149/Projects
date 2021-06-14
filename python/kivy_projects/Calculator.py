from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size=(600,700)

Builder.load_file("calc.kv")

class MyLayout(Widget):
    def clear_last(self):
        text = self.ids.calc_input.text
        text = text[:-1]
        self.ids.calc_input.text = text
        

    def clear(self):
        self.ids.calc_input.text = ""


    def add_number(self, i):
        if self.ids.calc_input.text == "0" or self.ids.calc_input.text == "ERROR" :
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
        num_list = text.split("+")
        num_list2 = text.split("*")
        num_list3 = text.split("-")
        num_list4 = text.split("/")

        if ("+" in text and "." not in num_list[-1]) \
                or ("/" in text and "." not in num_list4[-1])\
                or ("*" in text and "." not in num_list2[-1])\
                or ("-" in text and "." not in num_list3[-1]):
            self.ids.calc_input.text = self.ids.calc_input.text + "."
        elif "." in text:
            pass
        else:
            self.ids.calc_input.text = self.ids.calc_input.text + "."
    def equal(self):
        num = self.ids.calc_input.text

        try:
            answer = eval(num)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "ERROR"
    

class CalculatorApp(App):
    def build(self):
        
        return MyLayout()


if __name__ == "__main__":
    CalculatorApp().run()