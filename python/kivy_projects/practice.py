from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager

# define different screen 
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

Window.size = (800,600)
# kv = Builder.load_file("multiscreen.kv")
Builder.load_file("image_button.kv")


class MyLayout(Widget):
    checks = []
    
    def pressed_on(self):
        self.ids.label1.text = "Logged In"
        self.ids.button_image.source = "images/login3.png"


    def pressed_off(self):
        self.ids.label1.text = "Logged Off"
        self.ids.button_image.source = "images/login4.png"


    # def spinner_clicked(self, value):
    #     self.ids.clicked_label.text = f"You Selected {value}"


    # def checkbox_click(self, instance, value, toppings):
    #     if value == True:
    #         MyLayout.checks.append(toppings)
    #         tops = ''
    #         for x in MyLayout.checks:
    #             tops = tops +" "+ x
    #         self.ids.output_label.text = f"You selected: {tops}"
    #     else:
    #         MyLayout.checks.remove(toppings)
    #         tops = ''
    #         for x in MyLayout.checks:
    #             tops = tops +" "+ x
    #         self.ids.output_label.text = f"You selected: {tops}"

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
        # return kv

if __name__ == "__main__":
    PracticeApp().run()
