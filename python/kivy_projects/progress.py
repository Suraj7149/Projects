from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("progress.kv")

class MyLayout(Widget):
    def pressed(self):
        current = self.ids.progress_bar_id.value
        if current == 100:
            current = 0
            self.ids.label_id.text = "0% progress"

        current += 25
        progress = f'{current}% progress'
        self.ids.progress_bar_id.value = current
        self.ids.label_id.text = progress

class ProgressApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
        ProgressApp().run()