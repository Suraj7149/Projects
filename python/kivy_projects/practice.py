from os import terminal_size
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.size = (800,600)
Builder.load_file("check_boxes.kv")

class MyLayout(Widget):
    checks = []
    
    def checkbox_click(self, instance, value, toppings):
        if value == True:
            MyLayout.checks.append(toppings)
            tops = ''
            for x in MyLayout.checks:
                tops = tops +" "+ x
            self.ids.output_label.text = f"You selected: {tops}"
        else:
            MyLayout.checks.remove(toppings)
            tops = ''
            for x in MyLayout.checks:
                tops = tops +" "+ x
            self.ids.output_label.text = f"You selected: {tops}"

    # def selected(self, filename):
    #     try:
    #         self.ids.my_image.source = filename[0]
    #         #print(filename[0])
    #     except:
    #         pass

    # def slide_it(self, *args):
    #     self.slide_text.text = str(int(args[1]))
    #     self.slide_text.font_size = str(int(args[1]) * 5)
    pass

class PracticeApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    PracticeApp().run()
